from cslabman.models import Scripts, AccountRequests, Systems


def scriptgen():
  ac = AccountRequests.objects.all()
  print(ac.script_string)
  # CHRIS: This could be where the script is generated.
  # CHRIS: producing a string that is returned from a function.
  # CHRIS: Input will be from selection on AdminPortal AccountRequests.
  # CHRIS: The function will be called by an AdminPortal Action.
  # CHRIS: The action will A:)output a string in a db
  #                        B:)show a string for copy & paste