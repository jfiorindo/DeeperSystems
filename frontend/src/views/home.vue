<template>
    <div style="max-width: 1200px; margin: 0 auto; padding: 20px;">
        <h1 style="font-size: 32px; font-weight: bold; color: #2c3e50; margin-bottom: 28px; text-align: center;">Users Table</h1>

      <Button label="New User" icon="pi pi-plus" @click="showCreateForm" style="margin-bottom: 2rem;"/>
  
      <DataTable :value="users" dataKey="id" stripedRows responsiveLayout="scroll">
        <Column field="username" header="Username" :sortable="true" />
        <Column field="roles" header="Roles">
          <template #body="{ data }">
            <Tag v-for="role in data.roles" :key="role" :value="role" style="margin-right: 0.5rem; margin-bottom: 0.25rem" />
          </template>
        </Column>
        <Column field="preferences.timezone" header="Timezone" />
        <Column field="active" header="Is Active?">
          <template #body="{ data }">
            <Tag :value="data.active ? 'Yes' : 'No'" :severity="data.active ? 'success' : 'danger'" />
          </template>
        </Column>
        <Column header="Actions">
          <template #body="{ data }">
            <Button icon="pi pi-pencil" class="p-button-text mr-2" @click="editUser(data)" />
            <Button icon="pi pi-trash" class="p-button-text" @click="confirmDelete(data.id)" />
          </template>
        </Column>
      </DataTable>
  
      <UserForm v-model:visible="formVisible" :edit-data="selectedUser" @saved="loadUsers" />
      <ConfirmDialog />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import { useConfirm } from 'primevue/useconfirm'
  import { useToast } from 'primevue/usetoast'
  
  import UserForm from '../components/UserForm.vue'
  
  const users = ref([])
  const formVisible = ref(false)
  const selectedUser = ref(null)
  const confirm = useConfirm()
  const toast = useToast()
  
  const api = 'http://localhost:5000/users'
  
  const loadUsers = async () => {
  const res = await axios.get(api)
  users.value = res.data
  console.log('Users loaded:', users.value)  // 👈 adiciona essa linha
}
  
  const showCreateForm = () => {
    selectedUser.value = null
    formVisible.value = true
  }
  
  const editUser = (user) => {
    selectedUser.value = { ...user }
    formVisible.value = true
  }
  
  const confirmDelete = (id) => {
    confirm.require({
      message: 'Are you sure you want to delete this user?',
      acceptLabel: 'Yes',
      rejectLabel: 'No',
      icon: 'pi pi-exclamation-triangle',
      accept: async () => {
        await axios.delete(`${api}/${id}`)
        toast.add({ severity: 'success', summary: 'Deleted', detail: 'User successfully deleted', life: 3000 })
        loadUsers()
      }
    })
  }
  
  onMounted(loadUsers)
  </script>