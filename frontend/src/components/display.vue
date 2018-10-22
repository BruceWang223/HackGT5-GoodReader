<template>
    <div class="container" v-if="resData!=null" v-loading="isloading"
    element-loading-text="Loading..."
    element-loading-spinner="el-icon-loading"
    element-loading-background="rgba(0,0,0,0.8)">
		<div class="audio-player">
			<aplayer autoplaye
				:music="{
					title: 'Summary',
					src: resData.url,
					pic: 'https://pbs.twimg.com/profile_images/692405474986164224/NzcXa05I_400x400.png'
				}"/>
			<!-- <vue-audio :file="summaryFile"/> -->
		</div>
    	<div class="summary">
        	<label class="label-part">Summary</label>
        	<p class="summary">{{ resData.summarization }}</p>
        </div>
        <div class="keywords">
        	<label class="label-part">Keywords</label>
        	<ul>
        		<!--li v-for="(item, index) in resData.keywords" :key="index">
        			{{ item }}
        		</li-->
        		<li v-for="(item, index) in resData.entities" :key="index">
        			{{ item.type }} : {{ item.name }}
        		</li>
        	</ul>
        </div>
        <div class="topic">
        	<label class="label-part">Topic</label>
        	<ul>
        		<li v-for="(item, index) in resData.topics" :key="index">
        			{{ item.name }}
        		</li>
        	</ul>
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import aplayer from 'vue-aplayer'
//import VueAudio from 'vue-audio'

export default {
    data () {
    	return {
			
    	}
    },
    computed: {
    	...mapState({
    		resData: state => state.dataModule.resData,
    		isloading: state => state.dataModule.isloading
    	})
	},
	components: {
		aplayer,
		//'vue-audio': VueAudio
	}
    //props: {
    //	resData: {
    //		type: Object
    //	}
    //}
}
</script>

<style scoped>
.container {
	text-align: left;
}

.label-part {
	font-size: 2em;
	font-style: italic;
    font-variant: all-petite-caps;
    font-family: "Times New Roman", Times, serif;
    font-weight: 600;
}

.summary {
	font-family: "Times New Roman", Times, serif;
	font-size: 1em;
	font-weight: 300;
}
</style>
