# Import the prettytable library
from prettytable import PrettyTable
import random
def input_goals():
    goals = {}
    resources_goals()
    print("======SHORT=TERM=GOALS==============")
    while True:
        short_term = input("Enter your short term goal (enter 'done' when finished): ")
        if short_term.lower() == "done":
            break
        short_term_due_date = input("Enter the due date for your short term goal (MM/DD/YYYY): ")
        goals[short_term] = {
            "short_term_due_date": short_term_due_date,
            "medium_term_due_date": None,
            "long_term_due_date": None
        }
    resources_goals()
    print("======MEDIUM=TERM=GOALS=============")
    while True:
        medium_term = input("Enter your medium term goal (enter 'done' when finished): ")
        if medium_term.lower() == "done":
            break
        medium_term_due_date = input("Enter the due date for your medium term goal (MM/DD/YYYY): ")
        goals[medium_term] = {
            "short_term_due_date": None,
            "medium_term_due_date": medium_term_due_date,
            "long_term_due_date": None
        }
    resources_goals()
    print("======LONG=TERM=GOALS==============")
    while True:
        long_term = input("Enter your long term goal (enter 'done' when finished): ")
        if long_term.lower() == "done":
            break
        long_term_due_date = input("Enter the due date for your long term goal (MM/DD/YYYY): ")
        goals[long_term] = {
            "short_term_due_date": None,
            "medium_term_due_date": None,
            "long_term_due_date": long_term_due_date
        }

    return goals

def save_goals(goals):
    # Create a prettytable object
    table = PrettyTable()

    # Add the columns to the table
    table.field_names = ["Goal", "Due Date", "Term"]

    # Loop through the goals and add the rows to the table
    for goal, goal_info in goals.items():
        if goal_info["short_term_due_date"]:
            table.add_row([goal, goal_info["short_term_due_date"], "Short Term"])
        elif goal_info["medium_term_due_date"]:
            table.add_row([goal, goal_info["medium_term_due_date"], "Medium Term"])
        elif goal_info["long_term_due_date"]:
            table.add_row([goal, goal_info["long_term_due_date"], "Long Term"])

    # Save the goals and due dates to a file
    with open("goals.txt", "w") as f:
        f.write(table.get_string())

    # Print the goals and due dates
    print(table)

def resources_goals():
  list_of_goal_advice = { 1: "Set specific and measurable goals that align with your values and priorities.",
                         2: "Create a plan and schedule for achieving your goals.", 
                         3: "Break down your goals into smaller tasks and take action daily.",
                         4: "Monitor your progress and adjust your plan as needed.",
                         5: "Use a simple and clear process to reach your goals.",
                         6: "Celebrate your successes and learn from your challenges.",
                         7: "Surround yourself with supportive people who share your goals.",
                         8: "Be proactive and think about how you can improve your goals.",
                         9: "Be mindful of your time and energy. You can't do everything at once."
  }

  # select random goal advice from list_of_goal_advice
  goal_advice = random.choice(list_of_goal_advice)
  print("======RESOURCES=GOAL=ADVICE=========")
  print("\33[31m" + goal_advice + "\33[0m")

def main():
    goals = input_goals()
    save_goals(goals)

if __name__ == "__main__":
    main()