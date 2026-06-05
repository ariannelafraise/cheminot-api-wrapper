# Cheminot API Wrapper

A simple wrapper for cheminot's API to aid in registration automation.

> [!CAUTION]
> Registration automation may not be allowed; real usage of this wrapper is discouraged.
> 
> I made this for fun and API reverse engineering practice.

# Installation

```sh
pip install cheminot
```

# Usage

## Instanciation

```python
from cheminot import CheminotSession

cheminot = CheminotSession(
    AUTH_TOKEN,
    USER_AGENT,
    STUDENT_ID,
    PROGRAM_ID,
    SEMESTER_ID,
    "https://cheminotn.etsmtl.ca"
)
```

## Methods

```python
get_path_courses() # Retrieve the program's path's courses.
```
```python
get_course_available_groups(course_id: str) # Get available groups for a specific course.
```
```python
register_to_course(course_id: str, group_number: str, concentration: str) # Register to a course's group.
```
```python
unregister_from_course(course_id: str) # Unregister from a course.
```
```python
get_schedule() # Retrieve the current schedule.
```
```python
confirm_schedule() # Confirm/save the current schedule.
```

# Variables

## AUTH_TOKEN

The JWT authorization token associated with the session to be used in requests. It expires after 1 hour.

## USER_AGENT

The user to be used in requests.

## STUDENT_ID

The permanent student code.

## PROGRAM_ID

The code of the program.

## SEMESTER_ID

The semester's code.

Format: {YEAR}{SEMESTER_POSITION_IN_YEAR(1 for Winter, 2 for Summer and 3 for Fall)}

## CONCENTRATION_ID

Possible values:
- "TC" (for Tronc Commun) used for mandatory courses.
- "AX" (for Axe), used for optional courses.

# Endpoints

## Get path's courses

```
GET /api/Etudiant/{STUDENT_ID}/programme/{PROGRAM_ID}/cheminement?session={SEMESTER_ID}
```
## Get course's available groups

```
GET /api/CoursOfferts/{STUDENT_ID}/programme/{PROGRAM_ID}/cours/{COURSE_ID}?sessionInscr={SEMESTER_ID}
```
## Register to a course

```
POST /api/horaire/etudiant/{STUDENT_ID}/programme/{PROGRAM_ID}/horaire/add?session={SEMESTER_ID}&concentration={CONCENTRATION_ID}
Body: {"Sigle":"{COURSE_ID}","Groupe":"{GROUP_NUMBER}"}
```
## Unregister from a course

```
DELETE /api/horaire/etudiant/{STUDENT_ID}/programme/{PROGRAM_ID}/session/{SEMESTER_ID}/cours/{COURSE_ID}
```
## Get schedule

```
GET /api/horaire/etudiant/{STUDENT_ID}/programme/{PROGRAM_ID}/horaire?session={SEMESTER_ID}
```
## Confirm schedule

```
PUT /api/horaire/etudiant/{STUDENT_ID}/confirmation-horaire
Body: {"SessionInscr":{SEMESTER_ID},"ProgrammeId":"{PROGRAM_ID}"}
```
