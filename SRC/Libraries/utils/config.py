"""
Simulation Configuration Flags

This module defines global boolean flags that control the verbosity and output
behavior of the damage simulation system. These are useful for debugging, logging,
and controlling what gets printed or written to Excel during simulation runs.

Flags:
    - print_when_filling: Logs when `fill_gaps()` is called.
    - print_name_when_saving: Logs the name of each `DamageResult` when saving to Excel or database.
    - print_to_sheet_when_saving: Writes `DamageResult` data to Excel when saving.
    - print_when_adding: Logs the result of adding two `DamageResult` objects.
    - print_update: Enables step-by-step logging of the damage simulation (shots, reloads, etc.).
"""

print_when_filling = False  # Whether to print when calling the fill gaps function
print_name_when_saving = False  # Whether to print the name when saving to the sheet
print_to_sheet_when_saving = False  # Whether to print to the sheet when saving
print_when_adding = False  # Whether to print the output DamageResult when adding two DamageResult objects together
print_update = False  # Whether to print the current state of the damage simulation when calling update()
