from sqlalchemy import Date, ForeignKey, CheckConstraint, String
from sqlalchemy.orm import mapped_column, Mapped
from Enrollment import Enrollment


class LetterGrade(Enrollment):
    __tablename__ = "letter_grade"
    # I HAD put Integer after the table name, but apparently it picks that up from the parent PK.
    letterGradeid: Mapped[int] = mapped_column('letter_grade_id',
                                               ForeignKey("enrollments.enrollment_id",
                                                          ondelete="CASCADE"), primary_key=True)
    minSatisfactory: Mapped[str] = mapped_column('min_satisfactory', String, nullable=False)

    # __table_args__ = (UniqueConstraint("name", name="departments_uk_01"), )
    __table_args__ = (
        CheckConstraint(minSatisfactory.in_(['A', 'B', 'C', 'D', 'F'])),
    )
    __mapper_args__ = {"polymorphic_identity": "letter_grade"}

    def __init__(self, section, student, min_satisfactory: String):
        super().__init__(section, student)
        self.minSatisfactory = min_satisfactory

    def __str__(self):
        return f"LetterGrade Enrollment: {super().__str__()}, Grade: {self.minSatisfactory}"
