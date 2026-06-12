from enum import StrEnum

class RolePolicy(StrEnum):
    ADMIN = "admin"
    GURU = "guru"
    SISWA = "siswa"
    
class PermissionService:
    def has_role(self, user, role_name: str):
        return user.groups.filter(name=role_name).exists()
        
    def is_admin(self, user):
        return self.has_role(user, RolePolicy.ADMIN)

    def is_guru(self, user):
        return self.has_role(user, RolePolicy.GURU)
    
    def get_roles(self, user):
        groups = set(user.groups.values_list("name", flat=True))

        # return {
        #     RolePolicy.ADMIN: RolePolicy.ADMIN in groups,
        #     RolePolicy.GURU: RolePolicy.GURU in groups,
        #     RolePolicy.SISWA: RolePolicy.SISWA in groups,
        # }
        
        return {
            role: role in groups
            for role in RolePolicy # bisa loop karna StrEnum
        }