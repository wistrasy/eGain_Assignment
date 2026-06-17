from enum import Enum, auto
tracking_database = {
    "1": {
        "status": "In Warehouse A",
        "location": "Chicago",
        "update": "1 hr",
        "phone": "555-0143",
        "responsible_party": "Distributer A",
        "has_issue": False
    },
    "2": {
        "status": "In Transit",
        "location": "Denver",
        "update": "1 day",
        "phone": "555-0199",
        "responsible_party": "UPS Denver",
        "has_issue": True
    },
    "3": {
        "status": "Out for Delivery",
        "location": "Austin",
        "update": "5 days",
        "phone": "555-0122",
        "responsible_party": "USPS Austin",
        "has_issue": False
    }
}

class BotState(Enum):
    WELCOME = auto()          # Greet the user
    ASK_TRACKING = auto()     # Ask for the tracking number
    TUTORIAL = auto()         # Help find tracking number
    ASK_ANOTHER = auto()      # Ask if they want further help
    EXIT = auto()             # Exit message
    WAITING = auto()          # Wait for human rep (In progress)
    PORTAL = auto()           # Back to main help portal (In Progress)
    DONE = auto()             # Support complete

print("Hello, I see that you are checking on the status of your package.")
support_status = BotState.WELCOME

while support_status is not BotState.DONE:
    match support_status:
        case BotState.WELCOME:
            has_tracking = input("Do you have your tracking number available? (Y/N): ").strip()
            if has_tracking not in ["Y","y","yes"]:
                support_status = BotState.TUTORIAL
            else:
                support_status = BotState.ASK_TRACKING
        case BotState.ASK_TRACKING:
            while support_status is BotState.ASK_TRACKING:
                tracking_number = input("Please enter your tracking number or type (help) for help: ").strip()
                if tracking_number in tracking_database:
                    package_info = tracking_database[tracking_number]
                    if package_info["has_issue"]:
                        print(f"It seems that there was in issue while: {package_info["status"]} in {package_info["location"]}.")
                        print(f"You can contact the currently responsible party {package_info["responsible_party"]} at {package_info["phone"]}.")
                    else:
                        print(f"There has been no issue reported with your package. It is currently: {package_info["status"]} in {package_info["location"]}.")
                        print(f"The status was last updated {package_info["update"]} ago.")
                        print(f"You can contact the currently responsible party {package_info["responsible_party"]} at {package_info["phone"]} if this is concerning.")
                    support_status = BotState.ASK_ANOTHER
                elif tracking_number in ["h", "help"]:
                    support_status = BotState.TUTORIAL
                else:
                    print(f"The tracking number {tracking_number} is invalid, please check that it was entered correctly.")
        case BotState.ASK_ANOTHER:
            while support_status is BotState.ASK_ANOTHER:
                further_help = input("Do you require further assitance? Y/N: ").strip()
                if further_help not in ["Y","y","yes"]:
                    support_status = BotState.EXIT
                else:
                    option = input("Type 1 for help with another package, 2 to talk with a human representitive, or 3 to return to the main support portal: ").strip()
                    match option:
                        case "1":
                            support_status = BotState.ASK_TRACKING
                        case "2":
                            support_status = BotState.WAITING
                        case "3":
                            support_status = BotState.PORTAL
                        case _:
                            print("Invalid input.")
        case BotState.TUTORIAL:
            print("Imagine I am a tutorial for finding tracking numbers...")
            further_help = input("Were you able to find the number? Y/N: ").strip()
            if further_help not in ["Y","y","yes"]:
                support_status = BotState.ASK_ANOTHER
            else:
                support_status = BotState.ASK_TRACKING
        case BotState.WAITING:
            print("Thank you for your patience while waiting to speak to a representitive.")
            support_status = BotState.DONE
        case BotState.PORTAL:
            print("Welcome back to the main portal, what can I help you with?")
            support_status = BotState.DONE
        case BotState.EXIT:
            print("Thank you for your patience, we hope we were able to resolve your issue to your satisfaction!")
            support_status = BotState.DONE