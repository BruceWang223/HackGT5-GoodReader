<template>
    <!-- <el-upload
        class="upload-demo"
        drag
        action="http://localhost:3000/upload"
        accept=".txt, .pdf"
        :on-change="handleChange"
        :on-preview="handlePreview"
        :file-list="fileList"
        :limit="1"
        name="uploadFile"
        :auto-upload="false">
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">Drop file here or <em>click to upload</em></div>
        <div class="el-upload__tip" slot="tip">pdf/txt files with a size less than 500kb</div>
    </el-upload> -->
    <form action="/api/upload" method="post" enctype="multipart/form-data" @change="filesChange($event.target.name, $event.target.files)">
        <!-- Select file to upload: -->
        <div class="dropbox">
            
            <p class="input-tip">Drop file here or</p>
            <input class="input-file" type="file" name="fileToUpload" id="fileToUpload" accept=".pdf">
            <label for="fileToUpload" class="upload-label">Click to upload</label>
            
            <p v-if="filename!=''" class="chosen-file">Selected file: {{ filename }}</p>
        </div>
    </form>
</template>

<script>
import { uploadService } from '../utils'
export default {
    data () {
        return {
            fileList: [],
            filename: ''
        }
    },
    props: {
    },
    methods: {
        handleChange (file, fileList) {
            const formData = new FormData();
            formData.append('file', file, file.name);
            // console.log(formData);
            uploadService.upload(formData).then(response => console.log(response));
            this.fileList = fileList.slice(0, 1);
        },
        handlePreview (file) {
            // console.log(file);
            // console.log(file.raw);
        },
        filesChange(fieldName, fileList) {
            // console.log(document.querySelector('.input-file').value.split("\\"));
            // handle file changes
            this.filename = fileList[0].name;
            const formData = new FormData();
            if (!fileList.length) return;
            // append the files to FormData
            Array
                .from(Array(fileList.length).keys())
                .map(x => {
                formData.append(fieldName, fileList[x], fileList[x].name);
                });
            this.$emit('getFormData', formData);
            console.log("done in child")
            // uploadService.upload(formData).then(response => console.log(response));
        }
    }
}
</script>

<style scoped>
.dropbox {
    outline: 1px dashed dodgerblue; /* the dash box */
    outline-offset: -5px;
    background: white;
    color: dimgray;
    /*padding: 10px 10px;*/
    height: 100px; /* minimum height */
    /* width: 90%; */
    /* position: relative; */
    /* cursor: pointer; */
}

.input-file {
    opacity: 0; /*invisible but it's there! */
    margin-left: 10%;
    width: 27%;
    height: 100px;
    cursor: pointer;
    left: 0;
    /* display: inline; */
    opacity: 0;
    /* overflow: hidden; */
    position: absolute;
    /* z-index: -1; */
}

.input-file + label {
    cursor: pointer; /* 小手光标*/
}

.input-tip {
    display: inline-block;
    padding-top: 25px;
}

.upload-label {
    color: dodgerblue;
}

.chosen-file {
    margin-top: 40px;
}
</style>
