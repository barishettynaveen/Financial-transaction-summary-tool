"""
Demo script for Employee Attendance App
Demonstrates automated usage and testing of the attendance system
"""

import json
import os
from datetime import date, timedelta
from employee_attendance_app import EmployeeAttendanceApp

def create_sample_data():
    """Create sample attendance data for demonstration"""
    print("="*60)
    print("Creating Sample Attendance Data for Last 10 Days")
    print("="*60)

    app = EmployeeAttendanceApp()

    # Clear existing data for demo
    if os.path.exists(app.data_file):
        os.remove(app.data_file)

    app.attendance_records = {}

    # Generate sample data for last 10 days
    import random
    random.seed(42)  # For reproducible results

    statuses = ['Present', 'Absent', 'Leave']
    weights = [0.85, 0.10, 0.05]  # 85% present, 10% absent, 5% leave

    for i in range(10, 0, -1):
        record_date = str(date.today() - timedelta(days=i))
        app.attendance_records[record_date] = {}

        print(f"\n📅 Generating data for {record_date}...")

        for emp_id, emp_name in app.employees.items():
            status = random.choices(statuses, weights=weights)[0]
            app.attendance_records[record_date][emp_id] = {
                'name': emp_name,
                'status': status,
                'timestamp': f"{random.randint(8,9):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}"
            }
            print(f"  {emp_name} ({emp_id}): {status}")

    # Add today's attendance
    today = str(date.today())
    app.attendance_records[today] = {}
    print(f"\n📅 Generating data for {today} (Today)...")

    for emp_id, emp_name in app.employees.items():
        status = random.choices(statuses, weights=weights)[0]
        app.attendance_records[today][emp_id] = {
            'name': emp_name,
            'status': status,
            'timestamp': f"{random.randint(8,9):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}"
        }
        print(f"  {emp_name} ({emp_id}): {status}")

    app.save_data()
    print("\n✓ Sample data created successfully!")
    return app

def demo_view_today():
    """Demonstrate viewing today's attendance"""
    print("\n" + "="*60)
    print("DEMO: Viewing Today's Attendance")
    print("="*60)

    app = EmployeeAttendanceApp()
    app.view_today_attendance()

def demo_attendance_history():
    """Demonstrate viewing attendance history"""
    print("\n" + "="*60)
    print("DEMO: Viewing Attendance History")
    print("="*60)

    app = EmployeeAttendanceApp()
    app.view_attendance_history()

def demo_generate_report():
    """Demonstrate generating attendance report"""
    print("\n" + "="*60)
    print("DEMO: Generating Attendance Report")
    print("="*60)

    app = EmployeeAttendanceApp()
    app.generate_report()

def demo_search_employee():
    """Demonstrate searching employee attendance"""
    print("\n" + "="*60)
    print("DEMO: Searching Employee Attendance")
    print("="*60)

    app = EmployeeAttendanceApp()

    # Search for first employee
    emp_id = 'EMP001'
    emp_name = app.employees[emp_id]

    print(f"\n📊 Attendance Records for {emp_name} ({emp_id})")
    print("-" * 50)
    print(f"{'Date':<15} {'Status':<12} {'Time':<10}")
    print("-" * 50)

    for record_date in sorted(app.attendance_records.keys(), reverse=True):
        if emp_id in app.attendance_records[record_date]:
            record = app.attendance_records[record_date][emp_id]
            status_emoji = {'Present': '✓', 'Absent': '✗', 'Leave': '📅'}
            emoji = status_emoji.get(record['status'], '')
            print(f"{record_date:<15} {emoji} {record['status']:<10} {record.get('timestamp', 'N/A'):<10}")

def display_data_file():
    """Display the raw JSON data"""
    print("\n" + "="*60)
    print("Raw JSON Data Storage")
    print("="*60)

    if os.path.exists('attendance_data.json'):
        with open('attendance_data.json', 'r') as f:
            data = json.load(f)
            print(json.dumps(data, indent=2)[:1000] + "...")  # Show first 1000 chars
    else:
        print("No data file found!")

def run_all_demos():
    """Run all demonstration functions"""
    print("\n" + "="*60)
    print("🏢 EMPLOYEE ATTENDANCE APP - COMPLETE DEMONSTRATION")
    print("="*60)

    # Step 1: Create sample data
    create_sample_data()
    print("\n➡️  Viewing today's attendance...")

    # Step 2: View today's attendance
    demo_view_today()
    print("\n➡️  Viewing attendance history...")

    # Step 3: View history
    demo_attendance_history()
    print("\n➡️  Generating report...")

    # Step 4: Generate report
    demo_generate_report()
    print("\n➡️  Searching employee attendance...")

    # Step 5: Search employee
    demo_search_employee()
    print("\n➡️  Viewing raw data file...")

    # Step 6: Show raw data
    display_data_file()

    print("\n" + "="*60)
    print("✓ Demo Complete!")
    print("="*60)
    print("\nTo run the interactive app, execute:")
    print("  python employee_attendance_app.py")
    print("\nData is stored in: attendance_data.json")
    print("="*60)

if __name__ == "__main__":
    run_all_demos()
