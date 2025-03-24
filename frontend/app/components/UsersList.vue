<script setup lang="ts">
	interface User {
		username: string
		is_active: boolean
		email: string
	}

	const { data: users } = await useAPI<User[]>('/users', {
		method: 'get',
		onResponseError: (error) => {
			showErrorAlert('Failed to fetch users list')
		},
	})
</script>
<template>
	<div
		class="overflow-x-auto rounded-box border border-base-content/5 bg-base-100"
	>
		<table class="table">
			<thead>
				<tr>
					<th>Username</th>
					<th>Email</th>
					<th>Status</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(user, index) in users" :key="index">
					<td>{{ user.username }}</td>
					<td>{{ user.email }}</td>
					<td>
						<div v-if="user.is_active" class="badge-soft badge badge-success">
							Active
						</div>
						<div v-else class="badge-soft badge badge-error">Inactive</div>
					</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>
