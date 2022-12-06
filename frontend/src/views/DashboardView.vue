<template>
  <div>
    <navbar/>
    <div class="ms-250 me-20 pt-80 text-light" id="admin-pages">
      <div class="container-fluid">
        <div class="row h-50vh">
          <div class="col col-12 col-lg-6">
            <about/>
          </div>
          <div class="col col-12 col-lg-6">
            <skills/>
          </div>
          <div class="col col-12 col-lg-6">
            <div class="bg-dark my-4 my py-4">
                <p>salam</p>
                <p>salam</p>
                <p>salam</p>
                <p>salam</p>
            </div>

          </div>
          <div class="col col-12 col-lg-6">salam</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '../components/dashboard/blogs/Navbar.vue'
import About from '../components/dashboard/resume/About.vue'
import Skills from '../components/dashboard/resume/Skills.vue'
export default {
  components: { Navbar, About, Skills },
  name:"DashboardView",
  
  methods:{
    
  },
    created(){
   
  },
  
    
  
}
</script>

<style>
  
</style>