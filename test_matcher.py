from models.schemas import MatchRequest, JobRequirement, StudentProfile, Skill
from main import match_students_to_job
import json

def run_test():
    print("إعداد البيانات التجريبية (Mock Data)...")
    
    # الوظيفة المطلوبة: مطور React بميزانية محددة
    job = JobRequirement(
        id="job_001",
        location="Remote",
        max_budget=1000.0,
        required_skills=[
            Skill(name="React", level=4),
            Skill(name="TypeScript", level=3)
        ],
        required_languages=["Arabic", "English"],
        description="We are looking for a frontend developer to build interactive user interfaces using React and Typescript. Experience with state management and API integration is a plus."
    )

    # الطالب الأول: تطابق مثالي (تطابق الكلمات والمهارات والميزانية)
    student1 = StudentProfile(
        id="stu_perfect",
        location="Remote",
        expected_budget=800.0,
        skills=[
            Skill(name="React", level=5),
            Skill(name="TypeScript", level=4)
        ],
        languages=["Arabic", "English"],
        description="I am a frontend developer with strong experience in building React and TypeScript applications. I have worked on scalable UI components."
    )

    # الطالب الثاني: تطابق دلالي ممتاز (استخدم كلمة Next.js بدل React) لكن لديه مشكلة في الميزانية
    student2 = StudentProfile(
        id="stu_overbudget",
        location="Remote",
        expected_budget=1500.0, # أعلى من الميزانية (1000) - سيتم استبعاده رقمياً
        skills=[
            Skill(name="Next.js", level=4),
            Skill(name="JavaScript", level=4)
        ],
        languages=["Arabic", "English"],
        description="I love building modern web apps with Next.js and JavaScript. I enjoy creating fast and interactive frontend experiences."
    )

    # الطالب الثالث: الطالب المناسب دلالياً (استخدم NextJS بدل React) والميزانية مناسبة
    student3 = StudentProfile(
        id="stu_semantic_match",
        location="Remote",
        expected_budget=900.0,
        skills=[
            Skill(name="Next.js", level=4), # لاحظ لم يكتب React
            Skill(name="JavaScript", level=5) # لم يكتب TypeScript
        ],
        languages=["Arabic", "English"],
        description="I build awesome frontend projects using Next.js and JS. Creating interactive UIs and connecting APIs is my passion."
    )

    request = MatchRequest(job=job, students=[student1, student2, student3])

    print("بدء عملية المطابقة...")
    response = match_students_to_job(request)

    print("\n=== نتائج المطابقة ===")
    for match in response.matches:
        print(f"الطالب: {match.student_id}")
        print(f"  - درجة التطابق النهائي: {match.final_score * 100:.2f}%")
        print(f"  - التطابق الرقمي (المهارات/الميزانية): {match.deterministic_score * 100:.2f}%")
        print(f"  - التطابق الدلالي (الفهم الذكي): {match.semantic_score * 100:.2f}%")
        print("-" * 30)

if __name__ == "__main__":
    run_test()
