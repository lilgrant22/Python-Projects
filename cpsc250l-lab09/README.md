# Overview

In this lab we will be begin working in pairs using *pair programming*.

The lab will span four weeks.
For the first 3 labs, you should only work *during* your lab.
Your presence is require to receive credit.

If you are schedule to miss any days due to approved travel (e.g. sports), 
let your instructor know today so that pairing can be adjusted accordingly.


For Week 0 (today), we are only interested in a paper design.

*DO NOT START CODING TODAY!*

Following the example of the previous labs, I generated a number of data files.
Here is the output of my script:
<pre>
data/small_test
	 data/small_test/crn9001
         Generated  4  IDs in roster
         Expected grades median=76.57468396939561 mean=75.01162250194021 s.d.=9.767205923317595
         Total test grades = 8
         Total quiz grades = 32
         Total project grades = 8
	 data/small_test/crn9003
         Generated  3  IDs in roster
         Expected grades median=82.3199231549141 mean=82.06686742264871 s.d.=10.842371538764246
         Total test grades = 12
         Total quiz grades = 24
         Total project grades = 12
	 data/small_test/crn9002
         Generated  5  IDs in roster
         Expected grades median=75.26870877908279 mean=75.49302521750093 s.d.=4.730386792380698
         Total test grades = 15
         Total quiz grades = 15
         Total project grades = 10
data/grade_book
	 data/grade_book/crn9012
         Generated  25  IDs in roster
         Expected grades median=79.62756177734165 mean=79.70413541752896 s.d.=4.286219608916005
         Total test grades = 50
         Total quiz grades = 100
         Total project grades = 50
	 data/grade_book/crn9013
         Generated  30  IDs in roster
         Expected grades median=78.79432502389601 mean=78.0251644848876 s.d.=7.536109131756
         Total test grades = 60
         Total quiz grades = 90
         Total project grades = 60
	 data/grade_book/crn9011
         Generated  27  IDs in roster
         Expected grades median=73.51837674261533 mean=73.89715673859222 s.d.=5.325753510701368
         Total test grades = 54
         Total quiz grades = 216
         Total project grades = 54
</pre>


You are required to design and develop a `grade_book` application for a 
beleaguered professor.

I've given you this sample data to allow you to test 
your application prior to delivery to your lab instructor.

I've given you two sets of data: `small_test` and `grade_book`.
As its name implies, the data in `small_test` only contains a few names to make it easier to verify.

Each sub-folder is assigned to a different course section identified by CRN.
Within that CRN folder, the files of interest to you are `roster.csv` and the 
individual test (`T_*.csv`), quiz (`Q_*.csv`), and project (`P_*.csv`) files.

Your code should work with any similar folder/file structure.  
DO NOT hard code to these folder and file names.

The lab is worth 400 points in total distributed over the next four weeks.

The points will be distributed according to the following critera:

- 40 Points/week (160 total) - Presence, active participation, cooperation, and progress with assigned pair partner
- 60 Points Week 0 design of project
  * 10 points define plan for accessing data files and loading the data
  * 10 points define major inputs required of user, and strategy for managing choices 
  * 10 points define major methods and/or classes that need to be written
  * 10 points define data storage and access strategy
  * 10 points define calculation requirements and strategy
  * 10 points define three major development milestones that will be achieved week-by-week
- 60 Points Week 1 - Progress toward milestone 1
  * 30 points toward demonstrable progress on overall objectives
  * 20 points and identify necessary adjustments
  * 10 points identify realistic objectives for week 3
- 60 Points Week 2 - Progress toward milestone 2
  * 30 points toward demonstrable progress on overall objectives
  * 20 points and identify necessary adjustments
  * 10 points identify realistic objectives for week 4
- 60 Points Week 3 - Demonstrated correct functionality
  *  5 points load data and perform basic calculations (e.g. course statistics per assignment per CRN)
  * 10 points perform overall course calculations (e.g. weighted average per student and overal per CRN)
  * 20 points user selectable display of course statistics
  * 10 points user selectable display of individual student data 
  *  5 points properly handles missing data (see below requirements)
  *  5 points interface style and user friendliness
  *  5 points student handles surprise requirements given in later weeks
  
Good luck and have fun!

## Requirements

 ###This is a partial list
 * You will need to determine additional relevant requirements as part of your design.
 * Given an identified folder (e.g. `data/small_test`)
 * Read relevant data from all `CRN*` sub-folders
   * If an assignment is missing for a given student, assign a grade of 0 for that assignment
     * e.g. `elroy.korhonen.19` did not submit quiz 2 in `crn9001`
     * e.g. `jonah.lehrman.19`did not take test 1 in `crn9002`
 * Store in computer memory in manner you deem best 
 * Be able to display the following on demand:
   * assignment statistics (median, mean, standard deviation) per type (test, quiz, project) for each student
   * weighted grade per student (30% test mean, 30% quiz  mean, 40% project mean)
   * Overall grade for each assignment, and assignment type for each CRN 
      * e.g. what was the median of all students for test 3?  what was the mean for all tests in CRN9001
   * Instructor can choose which section (CRN) to show data for, and choose to display summary,or specific data
   for a student (by ID), or assignment.
   
## Directions

### Week 0

For today, you are only tasked with doing a design and planning.

To be clear.  Do NOT start coding this assignment until next week.   
All coding must completed in lab during the following two weeks. 
> NOTE: One exception would be you are allowed to continue debugging functions that you start,
> but do NOT add new functionality outside of class, and do NOT code without your partner present.

Today you will do a paper design by determining what the major steps are required, plan for methods that need to be 
written and possibly some classes to help organize your data.

Determine the flow of the program.

We are NOT defining any particular structure, nor are we providing unit tests.  
It is up to you to determine the design and to test your code for correctness.

This initial design work is to be your own effort, guided by the instructor as necessary.
Do your initial work on paper, and then edit the `design.md` file provided in this repository.

Answer the questions given in `design.md`, and identify the major milestones you will need to hit in order to deliver 
your final program on time by the end of Week 3.

You will edit this file as needed if your design changes during the coming weeks, and to update your milestones 
according to your actual progress.

The `design.md` file will function as a shared design notebook to document your ideas and progress.
Be sure to commit changes as you do with source code.

See https://docs.gitlab.com/ee/user/markdown.html for usage guide to formatting Markdown style text.
Formatting is suggested, but raw text is acceptable.


## Honor Code 

All work on this project is to be the independent work of you and your assigned pair programming partner.

Do NOT show your code to anyone else, nor bounce design ideas off of anyone else.

You *may* discuss general concepts (e.g. "how do I read data from file?") with other students under the 
*empty hands* rules, but you *must* document any help *given or received* in the `design.md` file. 

You are allowed to discuss the design with your lecture or lab instructors.

As this is an open ended project there is expected to be a wide variation of approaches to solving this problem.
Your code will be compared to others code, 
and anyone instances of shared code will be considered an honor code violation.

As all code is expected to be done together in the presence of your partner, 
both partners are accountable for receipt of shared of code.



