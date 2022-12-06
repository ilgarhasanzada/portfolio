<template>
  <div>
    <navbar/>
    <update-post/>
  </div>
</template>

<script>
import Navbar from '../../../components/dashboard/blogs/Navbar.vue'
import UpdatePost from '../../../components/dashboard/blogs/UpdatePost.vue'
export default {
  components: { UpdatePost, Navbar },
    name:"UpdateBlog"
}
</script>

<style>

</style>