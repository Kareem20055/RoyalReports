from datetime import time

from core.attendance.status import AttendanceStatus

from models.calculated_attendance import CalculatedAttendance
from models.summary import Summary


class SummaryCalculator:
    """
    Calculate summary information for a report.
    """

    def calculate(
        self,
        attendance: list[CalculatedAttendance],
    ) -> Summary:

        summary = Summary()

        check_in_total = 0
        check_in_count = 0

        check_out_total = 0
        check_out_count = 0

        for day in attendance:

            # Attendance status
            if day.status == AttendanceStatus.PRESENT:
                summary.present += 1

            elif day.status == AttendanceStatus.LATE:
                summary.late += 1

            elif day.status == AttendanceStatus.ABSENT:
                summary.absent += 1

            # Totals
            summary.worked_minutes += day.worked_minutes
            summary.late_minutes += day.late_minutes
            summary.early_leave_minutes += day.early_leave_minutes
            summary.overtime_minutes += day.overtime_minutes

            # Average Check In
            if day.check_in:

                t = day.check_in

                check_in_total += (
                    t.hour * 3600
                    + t.minute * 60
                    + t.second
                )

                check_in_count += 1

            # Average Check Out
            if day.check_out:

                t = day.check_out

                check_out_total += (
                    t.hour * 3600
                    + t.minute * 60
                    + t.second
                )

                check_out_count += 1

            if check_in_count:
                seconds = check_in_total // check_in_count

                summary.average_check_in = time(
                    hour=(seconds // 3600) % 24,
                    minute=(seconds % 3600) // 60,
                second=seconds % 60,
                )

            if check_out_count:
                seconds = check_out_total // check_out_count

                summary.average_check_out = time(
                    hour=(seconds // 3600) % 24,
                    minute=(seconds % 3600) // 60,
                    second=seconds % 60,
                )

        return summary