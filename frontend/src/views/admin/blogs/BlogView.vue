<template>
  <div>
    <navbar/>
    <div class="ms-250 me-20 pt-80 text-light" id="admin-pages">
      <blogs />
    </div>
    
  </div>
</template>

<script>
import Blogs from '../../../components/dashboard/blogs/Blogs.vue'
import Navbar from '../../../components/dashboard/blogs/Navbar.vue'
export default {
  components: { Blogs, Navbar },

}
</script>

<style>

</style>