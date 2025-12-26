"""
Rymal Variety Employee Attendance Tracking System
Tracks attendance with ability to add new employees
"""

import json
import os
from datetime import datetime, date
from typing import Dict, List

class RymalAttendanceApp:
    def __init__(self, data_file='rymal_attendance_data.json', employees_file='rymal_employees.json'):
        self.data_file = data_file
        self.employees_file = employees_file
        self.employees = self.load_employees()
        self.attendance_records = self.load_attendance_data()

    def load_employees(self) -> Dict:
        """Load employee data from JSON file"""
        if os.path.exists(self.employees_file):
            try:
                with open(self.employees_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return self.initialize_default_employees()
        return self.initialize_default_employees()

    def initialize_default_employees(self) -> Dict:
        """Initialize with default 4 employees"""
        default_employees = {
            'EMP001': 'Naveen',
            'EMP002': 'Damini',
            'EMP003': 'Muskan',
            'EMP004': 'Lina'
        }
        self.save_employees(default_employees)
        return default_employees

    def save_employees(self, employees=None):
        """Save employee data to JSON file"""
        if employees is None:
            employees = self.employees
        with open(self.employees_file, 'w') as f:
            json.dump(employees, f, indent=2)

    def load_attendance_data(self) -> Dict:
        """Load attendance data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_attendance_data(self):
        """Save attendance data to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.attendance_records, f, indent=2)

    def add_new_employee(self):
        """Add a new employee to the system"""
        print(f"\n{'='*50}")
        print("Add New Employee")
        print(f"{'='*50}\n")

        # Generate new employee ID
        if self.employees:
            max_id = max([int(emp_id.replace('EMP', '')) for emp_id in self.employees.keys()])
            new_id = f"EMP{max_id + 1:03d}"
        else:
            new_id = "EMP001"

        emp_name = input("Enter employee name: ").strip()

        if not emp_name:
            print("❌ Employee name cannot be empty!")
            return

        self.employees[new_id] = emp_name
        self.save_employees()

        print(f"\n✓ Employee added successfully!")
        print(f"Employee ID: {new_id}")
        print(f"Name: {emp_name}")

    def view_all_employees(self):
        """Display all employees"""
        print(f"\n{'='*50}")
        print("All Employees - Rymal Variety")
        print(f"{'='*50}\n")

        if not self.employees:
            print("❌ No employees found!")
            return

        print(f"{'Employee ID':<15} {'Name':<25} {'Status':<15}")
        print("-" * 55)

        for emp_id, emp_name in sorted(self.employees.items()):
            # Check if employee has any attendance record
            has_records = any(emp_id in records for records in self.attendance_records.values())
            status = "Active" if has_records else "Not started"
            print(f"{emp_id:<15} {emp_name:<25} {status:<15}")

        print(f"\nTotal Employees: {len(self.employees)}")

    def mark_attendance(self):
        """Mark attendance for all employees"""
        today = str(date.today())
        print(f"\n{'='*50}")
        print(f"Mark Attendance for {today}")
        print(f"{'='*50}\n")

        if not self.employees:
            print("❌ No employees found! Please add employees first.")
            return

        if today in self.attendance_records:
            print(f"⚠️  Attendance for {today} already recorded!")
            overwrite = input("Do you want to overwrite? (yes/no): ").lower()
            if overwrite != 'yes':
                return

        self.attendance_records[today] = {}

        for emp_id, emp_name in sorted(self.employees.items()):
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

        self.save_attendance_data()
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

        for emp_id, emp_name in sorted(self.employees.items()):
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
        print("Attendance History - Rymal Variety")
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

            for emp_id, emp_name in sorted(self.employees.items()):
                if emp_id in self.attendance_records[record_date]:
                    record = self.attendance_records[record_date][emp_id]
                    status_emoji = {'Present': '✓', 'Absent': '✗', 'Leave': '📅'}
                    emoji = status_emoji.get(record['status'], '')
                    print(f"{emp_id:<12} {emp_name:<20} {emoji} {record['status']:<10}")
                else:
                    print(f"{emp_id:<12} {emp_name:<20} {'Not marked':<10}")

    def generate_report(self):
        """Generate attendance summary report"""
        print(f"\n{'='*50}")
        print("Attendance Summary Report - Rymal Variety")
        print(f"{'='*50}\n")

        if not self.attendance_records:
            print("❌ No attendance records found!")
            return

        # Calculate statistics for each employee
        print(f"{'Employee ID':<12} {'Name':<20} {'Present':<10} {'Absent':<10} {'Leave':<10} {'Attendance %':<15}")
        print("-" * 77)

        for emp_id, emp_name in sorted(self.employees.items()):
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
        print(f"Total employees: {len(self.employees)}")

    def search_employee_attendance(self):
        """Search attendance for a specific employee"""
        print(f"\n{'='*50}")
        print("Search Employee Attendance")
        print(f"{'='*50}\n")

        if not self.employees:
            print("❌ No employees found!")
            return

        print("Available Employees:")
        for emp_id, emp_name in sorted(self.employees.items()):
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

        found_records = False
        for record_date in sorted(self.attendance_records.keys(), reverse=True):
            if emp_id in self.attendance_records[record_date]:
                found_records = True
                record = self.attendance_records[record_date][emp_id]
                status_emoji = {'Present': '✓', 'Absent': '✗', 'Leave': '📅'}
                emoji = status_emoji.get(record['status'], '')
                print(f"{record_date:<15} {emoji} {record['status']:<10} {record.get('timestamp', 'N/A'):<10}")

        if not found_records:
            print("No attendance records found for this employee.")

    def remove_employee(self):
        """Remove an employee from the system"""
        print(f"\n{'='*50}")
        print("Remove Employee")
        print(f"{'='*50}\n")

        if not self.employees:
            print("❌ No employees found!")
            return

        print("Current Employees:")
        for emp_id, emp_name in sorted(self.employees.items()):
            print(f"  {emp_id}: {emp_name}")

        emp_id = input("\nEnter Employee ID to remove: ").upper()

        if emp_id not in self.employees:
            print("❌ Invalid Employee ID!")
            return

        emp_name = self.employees[emp_id]
        confirm = input(f"Are you sure you want to remove {emp_name} ({emp_id})? (yes/no): ").lower()

        if confirm == 'yes':
            del self.employees[emp_id]
            self.save_employees()
            print(f"\n✓ Employee {emp_name} ({emp_id}) removed successfully!")
            print("Note: Past attendance records are preserved.")
        else:
            print("❌ Operation cancelled.")

    def display_menu(self):
        """Display main menu"""
        print(f"\n{'='*60}")
        print("🏢 RYMAL VARIETY - EMPLOYEE ATTENDANCE SYSTEM")
        print(f"{'='*60}")
        print("\n📋 Attendance Management")
        print("  1. Mark Today's Attendance")
        print("  2. View Today's Attendance")
        print("  3. View Attendance History")
        print("  4. Generate Attendance Report")
        print("  5. Search Employee Attendance")
        print("\n👥 Employee Management")
        print("  6. View All Employees")
        print("  7. Add New Employee")
        print("  8. Remove Employee")
        print("\n  9. Exit")
        print(f"{'='*60}")

    def run(self):
        """Main application loop"""
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-9): ")

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
                self.view_all_employees()
            elif choice == '7':
                self.add_new_employee()
            elif choice == '8':
                self.remove_employee()
            elif choice == '9':
                print("\n👋 Thank you for using Rymal Variety Attendance System!")
                break
            else:
                print("\n❌ Invalid choice! Please enter 1-9")

            input("\nPress Enter to continue...")


def main():
    """Main entry point"""
    print("\n" + "="*60)
    print("Welcome to Rymal Variety Employee Attendance System")
    print("="*60)

    app = RymalAttendanceApp()
    app.run()


if __name__ == "__main__":
    main()
