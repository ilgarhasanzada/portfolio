<template>
  <div>
    <navbar/>
    <div class="ms-250 me-20 pt-80" id="admin-pages">
        <new-post/>
    </div>
  </div>
</template>

<script>
import Navbar from '../../../components/dashboard/blogs/Navbar.vue'
import NewPost from '../../../components/dashboard/blogs/NewPost.vue'
export default {
  components: { NewPost, Navbar },
    name:'NewBlog'

}
</script>

<style>

</style>