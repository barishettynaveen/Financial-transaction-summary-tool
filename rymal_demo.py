"""
Demo script for Rymal Variety Attendance System
Demonstrates all features with automated sample data
"""

import json
import os
from datetime import date, timedelta
from rymal_attendance_app import RymalAttendanceApp

def cleanup_demo_files():
    """Remove existing demo files"""
    files = ['rymal_attendance_data.json', 'rymal_employees.json']
    for file in files:
        if os.path.exists(file):
            os.remove(file)
    print("Cleaned up existing demo files")

def create_sample_data():
    """Create sample attendance data"""
    print("="*60)
    print("Creating Sample Data for Rymal Variety Attendance System")
    print("="*60)

    app = RymalAttendanceApp()

    # Verify initial employees
    print("\n✓ Initial Employees Loaded:")
    for emp_id, emp_name in sorted(app.employees.items()):
        print(f"  {emp_id}: {emp_name}")

    # Add a new employee
    print("\n📝 Adding new employee 'Rajesh'...")
    max_id = max([int(emp_id.replace('EMP', '')) for emp_id in app.employees.keys()])
    new_id = f"EMP{max_id + 1:03d}"
    app.employees[new_id] = 'Rajesh'
    app.save_employees()
    print(f"✓ Added: {new_id} - Rajesh")

    # Generate sample attendance for last 10 days
    import random
    random.seed(42)

    statuses = ['Present', 'Absent', 'Leave']
    weights = [0.85, 0.10, 0.05]

    print("\n📅 Generating attendance records for last 10 days...")

    for i in range(10, 0, -1):
        record_date = str(date.today() - timedelta(days=i))
        app.attendance_records[record_date] = {}

        print(f"\n  Date: {record_date}")

        for emp_id, emp_name in sorted(app.employees.items()):
            status = random.choices(statuses, weights=weights)[0]
            app.attendance_records[record_date][emp_id] = {
                'name': emp_name,
                'status': status,
                'timestamp': f"{random.randint(8,9):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}"
            }
            status_emoji = {'Present': '✓', 'Absent': '✗', 'Leave': '📅'}
            emoji = status_emoji.get(status, '')
            print(f"    {emp_name}: {emoji} {status}")

    # Add today's attendance
    today = str(date.today())
    app.attendance_records[today] = {}
    print(f"\n  Date: {today} (Today)")

    for emp_id, emp_name in sorted(app.employees.items()):
        status = random.choices(statuses, weights=weights)[0]
        app.attendance_records[today][emp_id] = {
            'name': emp_name,
            'status': status,
            'timestamp': f"{random.randint(8,9):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}"
        }
        status_emoji = {'Present': '✓', 'Absent': '✗', 'Leave': '📅'}
        emoji = status_emoji.get(status, '')
        print(f"    {emp_name}: {emoji} {status}")

    app.save_attendance_data()
    print("\n✓ Sample data created successfully!")
    return app

def demo_view_all_employees(app):
    """Demonstrate viewing all employees"""
    print("\n" + "="*60)
    print("DEMO: View All Employees")
    print("="*60)
    app.view_all_employees()

def demo_view_today(app):
    """Demonstrate viewing today's attendance"""
    print("\n" + "="*60)
    print("DEMO: Today's Attendance")
    print("="*60)
    app.view_today_attendance()

def demo_attendance_history(app):
    """Demonstrate viewing attendance history"""
    print("\n" + "="*60)
    print("DEMO: Attendance History")
    print("="*60)
    app.view_attendance_history()

def demo_generate_report(app):
    """Demonstrate generating attendance report"""
    print("\n" + "="*60)
    print("DEMO: Attendance Report")
    print("="*60)
    app.generate_report()

def demo_search_employee(app):
    """Demonstrate searching employee attendance"""
    print("\n" + "="*60)
    print("DEMO: Search Employee Attendance (Naveen)")
    print("="*60)

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

def display_data_files(app):
    """Display the raw JSON data"""
    print("\n" + "="*60)
    print("Raw Data Storage")
    print("="*60)

    print("\n1. Employee Data (rymal_employees.json):")
    print("-" * 60)
    if os.path.exists(app.employees_file):
        with open(app.employees_file, 'r') as f:
            data = json.load(f)
            print(json.dumps(data, indent=2))

    print("\n2. Attendance Data (rymal_attendance_data.json) - Preview:")
    print("-" * 60)
    if os.path.exists(app.data_file):
        with open(app.data_file, 'r') as f:
            data = json.load(f)
            # Show first 2 dates
            preview = dict(list(data.items())[:2])
            print(json.dumps(preview, indent=2))
            print(f"\n... and {len(data) - 2} more dates")

def run_complete_demo():
    """Run complete demonstration"""
    print("\n" + "="*60)
    print("🏢 RYMAL VARIETY ATTENDANCE SYSTEM - COMPLETE DEMO")
    print("="*60)

    # Cleanup old files
    cleanup_demo_files()
    print()

    # Create sample data
    app = create_sample_data()
    print("\n" + "="*60)

    # Demo 1: View all employees
    demo_view_all_employees(app)
    print("\n" + "="*60)

    # Demo 2: View today's attendance
    demo_view_today(app)
    print("\n" + "="*60)

    # Demo 3: View history
    demo_attendance_history(app)
    print("\n" + "="*60)

    # Demo 4: Generate report
    demo_generate_report(app)
    print("\n" + "="*60)

    # Demo 5: Search employee
    demo_search_employee(app)
    print("\n" + "="*60)

    # Demo 6: Show raw data
    display_data_files(app)

    print("\n" + "="*60)
    print("✓ Demo Complete!")
    print("="*60)
    print("\n📌 Next Steps:")
    print("  1. Run the interactive app: python rymal_attendance_app.py")
    print("  2. Add new employees using option 7")
    print("  3. Mark daily attendance using option 1")
    print("\n💾 Data Files Created:")
    print("  - rymal_employees.json (Employee data)")
    print("  - rymal_attendance_data.json (Attendance records)")
    print("="*60)

if __name__ == "__main__":
    run_complete_demo()
