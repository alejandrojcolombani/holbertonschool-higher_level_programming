#!/usr/bin/python3
"""Module that generates personalized invitation files."""


def generate_invitations(template, attendees):
    """Generate invitation files using a template and attendee data.

    Args:
        template (str): Invitation template containing placeholders.
        attendees (list): List of dictionaries containing attendee data.
    """

    # Check that template is a string
    if not isinstance(template, str):
        print(
            f"Invalid input: template must be a string, "
            f"not {type(template).__name__}."
        )
        return

    # Check that attendees is a list
    if not isinstance(attendees, list):
        print(
            f"Invalid input: attendees must be a list, "
            f"not {type(attendees).__name__}."
        )
        return

    # Check that every attendee is a dictionary
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    # Check whether the template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check whether the attendee list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Generate one invitation for each attendee
    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        invitation = invitation.replace("{name}", str(name))
        invitation = invitation.replace("{event_title}", str(event_title))
        invitation = invitation.replace("{event_date}", str(event_date))
        invitation = invitation.replace(
            "{event_location}",
            str(event_location)
        )

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as output_file:
                output_file.write(invitation)
        except OSError as error:
            print(f"Error writing {filename}: {error}")
