import axios from 'axios'
import { createStore } from 'vuex'
export default createStore({
  state: {
    isAuthenticated:false,
    token:'',
    isLoading:false,
    blogs:[],
    tags:[],
    new_post:true,
    selected_post:null,
    about:[],
    skills:[],
    portfolios:[]
  },
  getters: {
    getSkills(state){
      return state.skills
    },
    getAbout(state){
      return state.about
    },
    getIsAuthenticated(state){
      return state.isAuthenticated
    },
    getBlogs(state){
      return state.blogs
    },
    getTags(state){
      return state.tags
    },
    getPortfolioLen(state){
      return state.portfolios.length
    }
  },
  mutations: {
    updateSkill(state, data){
      console.log(state, data)  
      state.skills[state.skills.indexOf(data.skill)].name=data.lang
    },
    setSkills(state, skills){
      state.skills=skills
    },
    setPortfolios(state, data){
      state.portfolios=data
    }
    ,
    updateAboutImage(state, image){
      state.about[0].image=image
    },
    setAbout(state, about){
      state.about=about
    },
    deleteSkill(state, skill){
      state.skills.splice(state.skills.indexOf(skill),1)
    }
    ,
    updateAbout(state, about){
      state.about[0]=about
    },
    setSelectedPost(state, post){
      console.log(post)
      state.selected_post=post
    },
    setNewData(state){
      // if (state.new_post){
        state.new_post=false
      // }else{
      //   state.new_post=true
      // }
  },
    setNewDataTrue(state){
      state.new_post=true
    },
    setTags(state, tags){
      state.tags=tags
    },
    setBlogs(state, blogs){
      state.blogs=blogs
    },
    updateBlog(state, blog){
      console.log(state.blogs.includes(blog))
    },
    deleteBlog(state,blog){
      state.blogs.splice(state.blogs.indexOf(blog),1)
    },
    addBlog(state,blog){
      state.blogs.unshift(blog)
    },
    deleteAllBlogs(state,blogs){
      for (const blog of blogs) {
        state.blogs.splice(state.blogs.indexOf(blog),1)
      }
    },
    initializeStore(state){
      if(localStorage.getItem('token')){
        state.token=localStorage.getItem('token')
        state.isAuthenticated=true
      }else{
        state.token='',
        state.isAuthenticated=false
      }
    },
    setIsLoading(state, status){
      state.isLoading = status
    },

    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },  
    
    removeToken(state) {
        state.token = ''
        state.isAuthenticated = false
    },
  },
  actions: {
    async fetchSkills({commit}){
      const data =await axios.get("about/skills/")
      commit('setSkills',data.data)
    },
    async fetchAbout({commit}){
      const data= await axios.get("about/")
      commit('setAbout',data.data)
    },
    async fetchTags({commit}){
      const data= await axios.get("blogs/tags/")
      commit('setTags',data.data)
    },
    async fetchBlogs({commit}){
      const blogs= await axios.get("blogs/")
      commit('setBlogs',blogs.data)
    },
    async fetchPortfolios({commit}){
      const data= await axios.get("portfolios/")
      commit('setPortfolios',data.data)
    },
    async actionDeleteBlog({commit},blog){
      await axios.delete('blogs/'+blog.id)
      commit('deleteBlog',blog)
    },
    async actionDeleteAllBlogs({commit},posts){
      for (const post of posts) {
        await axios.delete('blogs/'+post.id)
      }
      commit('deleteAllBlogs',posts)
    },
    actionAddBlog({commit},blog){
        commit('addBlog',blog)   
    },
    actionUpdateBlog({commit},blog){
      commit('updateBlog',blog)   
    },
    actionDeleteSkill({commit},data){
      commit('deleteSkill',data)   
    }
  },  
  modules: {

  }
})
