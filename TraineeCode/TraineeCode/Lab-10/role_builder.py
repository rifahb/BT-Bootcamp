class RoleBuilder:
    """
    Private data member
    """
    ROLES = ["UNDEFINED", "DEVELOPER", "TEST_ENGINEER", "SR_DEVELOPER", "DESIGNER"]

    """
    Method to get role description for a given role id
    """
    @staticmethod
    def get_role_description(role_id):
        try:
            idx = int(role_id)
        except (TypeError, ValueError):
            return "UNDEFINED"

        if 1 <= idx < len(RoleBuilder.ROLES):
            return RoleBuilder.ROLES[idx]
        return "UNDEFINED"
