from rest_framework import permissions



class ApiUserPermissions(permissions.BasePermission):

	SELECTED_GRUPO = "Backend"

	def has_permission(self,request,view):
		if request.user.groups.filter(
			name=self.SELECTED_GRUPO
			) and request.method == 'GET':
			return True

		return False 