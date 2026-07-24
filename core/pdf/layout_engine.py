from dataclasses import dataclass

from reportlab.pdfbase import pdfmetrics

from design.fonts import (
    ENGLISH_FONT,
    ARABIC_FONT,
    BODY_SIZE,
)

from design.layout import TABLE_CELL_PADDING

from i18n import is_rtl


@dataclass
class TableLayout:
    columns: list
    margin: float
    table_width: float
    label_width: float
    value_width: float


class LayoutEngine:

    @staticmethod
    def rtl() -> bool:
        return is_rtl()

    @staticmethod
    def text_align():
        return "right" if is_rtl() else "left"

    @staticmethod
    def text_x(cell_x, cell_width, padding):
        if is_rtl():
            return cell_x + cell_width - padding

        return cell_x + padding

    @staticmethod
    def page_start(page_width, margin):
        if is_rtl():
            return page_width - margin

        return margin

    @staticmethod
    def page_end(page_width, margin):
        if is_rtl():
            return margin

        return page_width - margin

    @staticmethod
    def section_start(page_width, margin, columns):
        table_width = sum(width for _, width in columns)

        if is_rtl():
            return page_width - margin - table_width

        return margin

    @staticmethod
    def available_width(page_width, margin):
        return page_width - (margin * 2)

    @staticmethod
    def label_width(
        labels,
        font_name,
        font_size,
        padding=20,
        minimum=110,
        maximum=220,
    ):
        widest = 0

        for label in labels:
            width = pdfmetrics.stringWidth(
                str(label),
                font_name,
                font_size,
            )

            widest = max(widest, width)

        return max(
            minimum,
            min(maximum, widest + padding),
        )

    @staticmethod
    def key_value_layout(
        labels,
        page_width,
        margin,
        font_name,
        font_size,
    ):
        table_width = LayoutEngine.available_width(
            page_width,
            margin,
        )

        label_width = LayoutEngine.label_width(
            labels,
            font_name,
            font_size,
        )

        value_width = table_width - label_width

        if is_rtl():
            columns = [
                ("value", value_width),
                ("label", label_width),
            ]
        else:
            columns = [
                ("label", label_width),
                ("value", value_width),
            ]

        return TableLayout(
            columns=columns,
            margin=LayoutEngine.section_start(
                page_width=page_width,
                margin=margin,
                columns=columns,
            ),
            table_width=table_width,
            label_width=label_width,
            value_width=value_width,
        )

    @staticmethod
    def data_table_layout(
        headers,
        rows,
        page_width,
        margin,
        weights=None,
        min_column_width=40,
        max_column_widths=None,
    ):
        """
        Create a responsive layout for data tables.
        """

        if weights is None:
            weights = [1] * len(headers)

        if len(headers) != len(weights):
            raise ValueError(
                "headers and weights must have the same length."
            )

        if max_column_widths is None:
            max_column_widths = [None] * len(headers)

        if len(headers) != len(max_column_widths):
            raise ValueError(
                "headers and max_column_widths must have the same length."
            )

        available_width = LayoutEngine.available_width(
            page_width,
            margin,
        )

        minimum_widths = []

        for column_index, header in enumerate(headers):

            texts = []

            for row in rows:
                if column_index < len(row):
                    texts.append(row[column_index])

            # لو العمود كله فاضي
            if not texts:
                texts.append("")

            width = LayoutEngine.minimum_text_width(
                texts=texts,
                font_name=LayoutEngine.font_name(),
                font_size=BODY_SIZE,
                padding=TABLE_CELL_PADDING,
            )

            width = max(min_column_width, width)

            max_width = max_column_widths[column_index]

            if max_width is not None:
                width = min(width, max_width)

            minimum_widths.append(width)

        minimum_total = sum(minimum_widths)

        if minimum_total > available_width:

            scale = available_width / minimum_total

            minimum_widths = [
                width * scale
                for width in minimum_widths
            ]

            minimum_total = available_width

        remaining_width = available_width - minimum_total
        unit = remaining_width / sum(weights)

        columns = []

        for header, minimum, weight in zip(
            headers,
            minimum_widths,
            weights,
        ):
            columns.append(
                (
                    header,
                    minimum + (weight * unit),
                )
            )

        return TableLayout(
            columns=columns,
            margin=LayoutEngine.section_start(
                page_width=page_width,
                margin=margin,
                columns=columns,
            ),
            table_width=available_width,
            label_width=0,
            value_width=0,
        )

    @staticmethod
    def minimum_text_widths(
        texts,
        font_name,
        font_size,
        padding,
    ):
        """
        Calculate the minimum width required for each text.
        """

        widths = []

        for text in texts:
            widths.append(
                pdfmetrics.stringWidth(
                    str(text),
                    font_name,
                    font_size,
                )
                + (padding * 2)
            )

        return widths

    @staticmethod
    def minimum_text_width(
        texts,
        font_name,
        font_size,
        padding,
    ):
        return max(
            pdfmetrics.stringWidth(
                str(text),
                font_name,
                font_size,
            )
            + (padding * 2)
            for text in texts
        )

    @staticmethod
    def font_name():
        return ARABIC_FONT if is_rtl() else ENGLISH_FONT