# Employee Attendance Tracking System

A simple and efficient command-line application to track attendance for 5 employees.

## Features

- **Mark Daily Attendance**: Record attendance status (Present/Absent/Leave) for all 5 employees
- **View Today's Attendance**: Display current day's attendance records
- **Attendance History**: View past attendance records
- **Generate Reports**: Get attendance summary with statistics and percentages
- **Search Employee Records**: Look up attendance history for individual employees
- **Persistent Storage**: All data is saved in JSON format for easy access

## Employees

The system tracks attendance for the following 5 employees:

1. **EMP001** - John Smith
2. **EMP002** - Sarah Johnson
3. **EMP003** - Michael Brown
4. **EMP004** - Emily Davis
5. **EMP005** - David Wilson

## Installation

No additional dependencies required! Uses only Python standard library.

```bash
python employee_attendance_app.py
```

## Usage

### Running the Application

```bash
python employee_attendance_app.py
```

### Menu Options

1. **Mark Today's Attendance**
   - Enter P (Present), A (Absent), or L (Leave) for each employee
   - Automatically saves with timestamp
   - Prevents duplicate entries for the same day

2. **View Today's Attendance**
   - Shows formatted table with all employee statuses
   - Displays time of attendance marking

3. **View Attendance History**
   - Shows last 10 days of attendance records
   - Organized by date in descending order

4. **Generate Attendance Report**
   - Summary statistics for each employee
   - Includes Present/Absent/Leave counts
   - Calculates attendance percentage
   - Shows total working days

5. **Search Employee Attendance**
   - Filter records by specific employee ID
   - Complete attendance history for selected employee

6. **Exit**
   - Safely close the application

## Data Storage

- Attendance data is stored in `attendance_data.json`
- JSON format for easy readability and portability
- Automatic save on each attendance entry

## Example Output

```
==================================================
🏢 EMPLOYEE ATTENDANCE TRACKING SYSTEM
==================================================

1. Mark Today's Attendance
2. View Today's Attendance
3. View Attendance History
4. Generate Attendance Report
5. Search Employee Attendance
6. Exit
==================================================
```

## Sample Attendance Report

```
Employee ID  Name                 Present    Absent     Leave      Attendance %
-----------------------------------------------------------------------------
EMP001       John Smith           18         2          0          90.00%
EMP002       Sarah Johnson        19         1          0          95.00%
EMP003       Michael Brown        17         2          1          85.00%
EMP004       Emily Davis          20         0          0          100.00%
EMP005       David Wilson         16         3          1          80.00%

Total working days recorded: 20
```

## Features Highlight

- Simple and intuitive CLI interface
- Real-time data persistence
- Comprehensive reporting capabilities
- Error handling for invalid inputs
- Timestamp tracking for audit purposes
- Attendance percentage calculation

## Technical Details

- **Language**: Python 3.x
- **Storage**: JSON file-based
- **Dependencies**: None (uses standard library only)
- **File**: employee_attendance_app.py

## Future Enhancements

Potential features for future versions:
- Date range filtering
- Export to CSV/Excel
- Email notifications for absences
- GUI interface
- Multi-month reporting
- Holiday calendar integration
