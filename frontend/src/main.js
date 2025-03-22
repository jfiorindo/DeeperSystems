import { createApp } from 'vue'
import App from './App.vue'

import PrimeVue from 'primevue/config'
import DialogService from 'primevue/dialogservice'
import ConfirmationService from 'primevue/confirmationservice'
import ToastService from 'primevue/toastservice'

import Button from 'primevue/button'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import Tag from 'primevue/tag'
import Dialog from 'primevue/dialog'
import ConfirmDialog from 'primevue/confirmdialog'
import InputText from 'primevue/inputtext'
import MultiSelect from 'primevue/multiselect'
import InputSwitch from 'primevue/inputswitch'
import Toast from 'primevue/toast'

import 'primevue/resources/themes/lara-light-indigo/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'

const app = createApp(App)

app.use(PrimeVue)
app.use(DialogService)
app.use(ConfirmationService)
app.use(ToastService)

app.component('Button', Button)
app.component('DataTable', DataTable)
app.component('Column', Column)
app.component('Tag', Tag)
app.component('Dialog', Dialog)
app.component('ConfirmDialog', ConfirmDialog)
app.component('InputText', InputText)
app.component('MultiSelect', MultiSelect)
app.component('InputSwitch', InputSwitch)
app.component('Toast', Toast)

app.mount('#app')
