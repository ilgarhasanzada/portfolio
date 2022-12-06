import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import store from '@/store'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
     component: () => import( '../views/AboutView.vue')
  },
  {
    path: '/portfolio',
    name: 'portfolio',
    component: () => import( '../views/PortfolioView.vue')
  },
  {
    path: '/contact',
    name: 'contact',
    component: () => import('../views/ContactView.vue')
  },
  {
    path: '/blog',
    name: 'blog',
    component: () => import( '../views/BlogView.vue')
  },
  {
    path: '/admin/resume',
    name: 'resume',
    component: () => import( '../views/DashboardView.vue'),
    beforeEnter:(to, from, next)=>{
      if(store.state.isAuthenticated){
        next()
      }else{
        next()
      }
    }
  },
  {
    path: '/admin/login',
    name: 'login',
    component: () => import( '../views/SignIn.vue'),
    beforeEach:(to, from, next)=>{
      if(store.state.isAuthenticated){
        next('/')
      }else{
        next()
      }
    }
  },
  {
    path: '/admin/messages',
    name: 'admin-messages',
    component: () => import( '../views/admin/MessageView.vue')
  },
  {
    path: '/admin/portfolios',
    name: 'admin-portfolios',
    component: () => import( '../views/admin/portfolios/PortfolioView.vue')
  },
  {
    path: '/admin/messages',
    name: 'admin-messages',
    component: () => import( '../views/admin/MessageView.vue')
  },
  {
    path: '/admin/blogs',
    name: 'admin-blogs',
    component: () => import( '../views/admin/blogs/BlogView.vue')
  },
  {
    path: '/admin/blog',
    name: 'new-blog',
    component: () => import( '../views/admin/blogs/NewBlog.vue')
  },
  {
    path: '/admin/blogs/:id',
    name: 'blog-detail',
    component: () => import( '../views/admin/blogs/UpdateBlog.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
