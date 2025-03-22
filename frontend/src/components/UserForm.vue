<template>
    <Dialog :visible="visible" @update:visible="val => emit('update:visible', val)" :header="editData ? 'Edit User' : 'New User'" :modal="true" :closable="true" :style="{ width: '30rem' }">
      <div class="p-fluid">
        <div class="field">
          <label for="username">Username</label>
          <InputText id="username" v-model="form.username" />
        </div>
  
        <div class="field">
          <label for="password">Password</label>
          <InputText id="password" v-model="form.password" />
        </div>
  
        <div class="field">
          <label>Roles</label>
          <MultiSelect v-model="form.roles" :options="availableRoles" optionLabel="label" optionValue="value" />
        </div>
  
        <div class="field">
          <label for="timezone">Timezone</label>
          <InputText id="timezone" v-model="form.preferences.timezone" />
        </div>
  
        <div class="field">
          <label for="active">Active</label>
          <InputSwitch v-model="form.active" />
        </div>
      </div>
  
      <template #footer>
        <Button label="Cancel" icon="pi pi-times" @click="emit('update:visible', false)" class="p-button-text" />
        <Button label="Save" icon="pi pi-check" @click="saveUser" autofocus />
      </template>
    </Dialog>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue'
  import axios from 'axios'
  import { useToast } from 'primevue/usetoast'
  
  const props = defineProps({
    visible: Boolean,
    editData: Object
  })
  const emit = defineEmits(['update:visible', 'saved'])
  
  const toast = useToast()
  
  const form = ref({
    username: '',
    password: '',
    roles: [],
    preferences: { timezone: '' },
    active: true
  })
  
  const availableRoles = [
    { label: 'admin', value: 'admin' },
    { label: 'manager', value: 'manager' },
    { label: 'tester', value: 'tester' }
  ]
  
  const api = 'http://localhost:5000/users'
  
  watch(() => props.editData, (newData) => {
    if (newData) form.value = { ...newData }
    else resetForm()
  })
  
  const resetForm = () => {
    form.value = {
      username: '',
      password: '',
      roles: [],
      preferences: { timezone: '' },
      active: true
    }
  }
  
  const saveUser = async () => {
    try {
      if (props.editData && props.editData.id) {
        await axios.put(`${api}/${props.editData.id}`, form.value)
        toast.add({ severity: 'success', summary: 'Updated', detail: 'User successfully updated', life: 3000 })
      } else {
        await axios.post(api, form.value)
        toast.add({ severity: 'success', summary: 'Created', detail: 'User successfully Created', life: 3000 })
      }
      emit('saved')
      emit('update:visible', false)
      resetForm()
    } catch (err) {
      toast.add({ severity: 'error', summary: 'Erro', detail: 'Failed to save user', life: 3000 })
    }
  }
  </script>