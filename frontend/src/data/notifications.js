import { createResource } from 'frappe-ui'

export let unreadNotifications = createResource({
  cache: 'Unread Notifications Count',
  url: 'politihub.api.unread_notifications',
  initialData: 0,
  auto: true,
})
