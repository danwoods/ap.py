"""defaults

Model for all functions:

Accept:
            All values allowed in a table row, passed as form data (for single) or a json string (for single or multiple)

Procedure:
  1. Validate:
    1.1 Check if feilds given are enough to satisfy all non-null and w/o default row feilds
  2. Assemble data for Model call
  3. Attempt Model call
  4. Return Success/Failure in requested format, in most informative representation
    
    
Return (all as variables in a 'results' variable): 
            0/1 for Delete
            0/id for Create
            0/json for Get,Set


"""

def Create():
  """Create: Creates new row"""
  pass

def Get():
  """Get: Returns requested data for given ids"""
  pass

def Set():
  """Set: Sets given feilds for given ids"""
  pass

def Delete():
  """Delete: Deletes one row"""
  pass
