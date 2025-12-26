# Rymal Variety - Employee Attendance Tracking System

A comprehensive employee attendance management system for Rymal Variety with the ability to add and manage employees dynamically.

## Features

### Attendance Management
- Mark daily attendance (Present/Absent/Leave)
- View today's attendance with timestamps
- Browse complete attendance history
- Generate detailed attendance reports with statistics
- Search individual employee attendance records

### Employee Management
- View all employees with their status
- Add new employees dynamically
- Remove employees from the system
- Automatic employee ID generation
- Persistent employee and attendance data storage

## Initial Employees

The system comes pre-configured with 4 employees:

1. **EMP001** - Naveen
2. **EMP002** - Damini
3. **EMP003** - Muskan
4. **EMP004** - Lina

## Adding New Employees

When a new employee joins:
1. Select option 7 from the main menu
2. Enter the employee's name
3. System automatically generates a unique Employee ID
4. Employee is immediately available for attendance tracking

## Installation

No additional dependencies required! Uses only Python standard library.

```bash
python rymal_attendance_app.py
```

## Usage

### Running the Application

```bash
python rymal_attendance_app.py
```

### Menu Options

**📋 Attendance Management**
1. Mark Today's Attendance - Record attendance for all employees
2. View Today's Attendance - See current day's records
3. View Attendance History - Browse past 10 days
4. Generate Attendance Report - Detailed statistics for all employees
5. Search Employee Attendance - View specific employee's history

**👥 Employee Management**
6. View All Employees - List all employees with status
7. Add New Employee - Register a new joining employee
8. Remove Employee - Remove an employee (preserves past records)

9. Exit - Close the application

## Data Storage

The system uses two JSON files:

- **rymal_employees.json** - Stores employee information
- **rymal_attendance_data.json** - Stores all attendance records

Both files are created automatically on first run.

## Example Attendance Report

```
==================================================
Attendance Summary Report - Rymal Variety
==================================================

Employee ID  Name                 Present    Absent     Leave      Attendance %
-----------------------------------------------------------------------------
EMP001       Naveen               18         2          0          90.00%
EMP002       Damini               19         1          0          95.00%
EMP003       Muskan               17         2          1          85.00%
EMP004       Lina                 20         0          0          100.00%
EMP005       Rajesh               5          0          0          100.00%

Total working days recorded: 20
Total employees: 5
```

## Adding a New Employee - Example

```
==================================================
Add New Employee
==================================================

Enter employee name: Rajesh

✓ Employee added successfully!
Employee ID: EMP005
Name: Rajesh
```

## Key Features

- **Dynamic Employee Management**: Add or remove employees anytime
- **Automatic ID Generation**: Sequential employee IDs assigned automatically
- **Data Persistence**: All data saved in JSON format
- **Historical Records**: Past attendance preserved even after employee removal
- **User-Friendly Interface**: Simple menu-driven system
- **Comprehensive Reports**: Detailed statistics and percentages
- **Timestamp Tracking**: Records exact time of attendance marking

## System Requirements

- Python 3.x
- No external dependencies

## File Structure

```
rymal_attendance_app.py       # Main application
rymal_employees.json          # Employee data (auto-generated)
rymal_attendance_data.json    # Attendance records (auto-generated)
```

## How It Works

1. **First Run**: System initializes with 4 default employees
2. **Add Employees**: New joiners can be added anytime with auto-generated IDs
3. **Mark Attendance**: Daily attendance tracked with timestamps
4. **Generate Reports**: View statistics, percentages, and trends
5. **Search Records**: Look up individual employee history

## Benefits

- Easy to use for HR departments
- Scalable - add unlimited employees
- No database required - simple JSON storage
- Complete audit trail with timestamps
- Attendance percentage calculations
- Historical data preservation

## Support

For issues or questions, please refer to the application menu or documentation.

---

**Rymal Variety Employee Attendance System**
Built with Python | Simple, Efficient, Reliable
