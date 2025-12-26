"""
Employee Attendance Tracking Application
Tracks attendance for 5 employees with features for marking, viewing, and reporting
"""

import json
import os
from datetime import datetime, date
from typing import Dict, List

class EmployeeAttendanceApp:
    def __init__(self, data_file='attendance_data.json'):
        self.data_file = data_file
        self.employees = {
            'EMP001': 'John Smith',
            'EMP002': 'Sarah Johnson',
            'EMP003': 'Michael Brown',
            'EMP004': 'Emily Davis',
            'EMP005': 'David Wilson'
        }
        self.attendance_records = self.load_data()

    def load_data(self) -> Dict:
        """Load attendance data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_data(self):
        """Save attendance data to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.attendance_records, f, indent=2)

    def mark_attendance(self):
        """Mark attendance for all employees"""
        today = str(date.today())
        print(f"\n{'='*50}")
        print(f"Mark Attendance for {today}")
        print(f"{'='*50}\n")

        if today in self.attendance_records:
            print(f"⚠️  Attendance for {today} already recorded!")
            overwrite = input("Do you want to overwrite? (yes/no): ").lower()
            if overwrite != 'yes':
                return

        self.attendance_records[today] = {}

        for emp_id, emp_name in self.employees.items():
            while True:
                status = input(f"{emp_name} ({emp_id}) - Present (P) / Absent (A) / Leave (L): ").upper()
                if status in ['P', 'A', 'L']:
                    full_status = {'P': 'Present', 'A': 'Absent', 'L': 'Leave'}[status]
                    self.attendance_records[today][emp_id] = {
                        'name': emp_name,
                        'status': full_status,
                        'timestamp': datetime.now().strftime('%H:%M:%S')
                    }
                    break
                else:
                    print("Invalid input! Please enter P, A, or L")

        self.save_data()
        print("\n✓ Attendance marked successfully!")

    def view_today_attendance(self):
        """Display today's attendance"""
        today = str(date.today())
        print(f"\n{'='*50}")
        print(f"Today's Attendance - {today}")
        print(f"{'='*50}\n")

        if today not in self.attendance_records:
            print("❌ No attendance record found for today!")
            return

        print(f"{'Employee ID':<12} {'Name':<20} {'Status':<12} {'Time':<10}")
        print("-" * 54)

        for emp_id, emp_name in self.employees.items():
            if emp_id in self.attendance_records[today]:
                record = self.attendance_records[today][emp_id]
                status_emoji = {'Present': '✓', 'Absent': '✗', 'Leave': '📅'}
                emoji = status_emoji.get(record['status'], '')
                print(f"{emp_id:<12} {emp_name:<20} {emoji} {record['status']:<10} {record['timestamp']:<10}")
            else:
                print(f"{emp_id:<12} {emp_name:<20} {'Not marked':<12}")

    def view_attendance_history(self):
        """Display attendance history"""
        print(f"\n{'='*50}")
        print("Attendance History")
        print(f"{'='*50}\n")

        if not self.attendance_records:
            print("❌ No attendance records found!")
            return

        # Show last 10 records
        dates = sorted(self.attendance_records.keys(), reverse=True)[:10]

        for record_date in dates:
            print(f"\n📅 Date: {record_date}")
            print("-" * 54)
            print(f"{'Employee ID':<12} {'Name':<20} {'Status':<12}")
            print("-" * 54)

            for emp_id, emp_name in self.employees.items():
                if emp_id in self.attendance_records[record_date]:
                    record = self.attendance_records[record_date][emp_id]
                    status_emoji = {'Present': '✓', 'Absent': '✗', 'Leave': '📅'}
                    emoji = status_emoji.get(record['status'], '')
                    print(f"{emp_id:<12} {emp_name:<20} {emoji} {record['status']:<10}")

    def generate_report(self):
        """Generate attendance summary report"""
        print(f"\n{'='*50}")
        print("Attendance Summary Report")
        print(f"{'='*50}\n")

        if not self.attendance_records:
            print("❌ No attendance records found!")
            return

        # Calculate statistics for each employee
        print(f"{'Employee ID':<12} {'Name':<20} {'Present':<10} {'Absent':<10} {'Leave':<10} {'Attendance %':<15}")
        print("-" * 77)

        for emp_id, emp_name in self.employees.items():
            present_count = 0
            absent_count = 0
            leave_count = 0
            total_days = 0

            for date_record in self.attendance_records.values():
                if emp_id in date_record:
                    total_days += 1
                    status = date_record[emp_id]['status']
                    if status == 'Present':
                        present_count += 1
                    elif status == 'Absent':
                        absent_count += 1
                    elif status == 'Leave':
                        leave_count += 1

            if total_days > 0:
                attendance_percentage = (present_count / total_days) * 100
            else:
                attendance_percentage = 0.0

            print(f"{emp_id:<12} {emp_name:<20} {present_count:<10} {absent_count:<10} {leave_count:<10} {attendance_percentage:.2f}%")

        print(f"\nTotal working days recorded: {len(self.attendance_records)}")

    def search_employee_attendance(self):
        """Search attendance for a specific employee"""
        print(f"\n{'='*50}")
        print("Search Employee Attendance")
        print(f"{'='*50}\n")

        print("Available Employees:")
        for emp_id, emp_name in self.employees.items():
            print(f"  {emp_id}: {emp_name}")

        emp_id = input("\nEnter Employee ID: ").upper()

        if emp_id not in self.employees:
            print("❌ Invalid Employee ID!")
            return

        emp_name = self.employees[emp_id]
        print(f"\n📊 Attendance Records for {emp_name} ({emp_id})")
        print("-" * 50)
        print(f"{'Date':<15} {'Status':<12} {'Time':<10}")
        print("-" * 50)

        for record_date in sorted(self.attendance_records.keys(), reverse=True):
            if emp_id in self.attendance_records[record_date]:
                record = self.attendance_records[record_date][emp_id]
                status_emoji = {'Present': '✓', 'Absent': '✗', 'Leave': '📅'}
                emoji = status_emoji.get(record['status'], '')
                print(f"{record_date:<15} {emoji} {record['status']:<10} {record.get('timestamp', 'N/A'):<10}")

    def display_menu(self):
        """Display main menu"""
        print(f"\n{'='*50}")
        print("🏢 EMPLOYEE ATTENDANCE TRACKING SYSTEM")
        print(f"{'='*50}")
        print("\n1. Mark Today's Attendance")
        print("2. View Today's Attendance")
        print("3. View Attendance History")
        print("4. Generate Attendance Report")
        print("5. Search Employee Attendance")
        print("6. Exit")
        print(f"{'='*50}")

    def run(self):
        """Main application loop"""
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-6): ")

            if choice == '1':
                self.mark_attendance()
            elif choice == '2':
                self.view_today_attendance()
            elif choice == '3':
                self.view_attendance_history()
            elif choice == '4':
                self.generate_report()
            elif choice == '5':
                self.search_employee_attendance()
            elif choice == '6':
                print("\n👋 Thank you for using the Attendance System!")
                break
            else:
                print("\n❌ Invalid choice! Please enter 1-6")

            input("\nPress Enter to continue...")


def main():
    """Main entry point"""
    print("\n" + "="*50)
    print("Welcome to Employee Attendance Tracking System")
    print("="*50)

    app = EmployeeAttendanceApp()
    app.run()


if __name__ == "__main__":
    main()
