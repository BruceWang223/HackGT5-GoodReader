<template>
    <div>
        <el-select v-model="value" placeholder="Select" class="select">
            <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
            </el-option>
        </el-select>

        <!-- <p>{{ value }}</p> -->
        <div class="input-part">
            <div v-if="value==='op1'">
                <upload v-on:getFormData="getFormData"></upload>
            </div>
            <div v-else-if="value=='op2'">
                <el-input
                    class="paste-part"
                    type="textarea"
                    :autosize="{ minRows: 2, maxRows: 8}"
                    placeholder="Please input"
                    v-model="pastearea">
                </el-input>
                <!-- <p>{{ pastearea }}</p> -->
            </div>
            <div v-else-if="value=='op3'">
                <el-input class="URL-part" placeholder="Please input" v-model="URLarea"></el-input>
                <!-- <p>{{ URLarea }}</p> -->
            </div>
        </div>

        <el-button type="primary" round class="submit" @click="submit">Submit</el-button>
    </div>
</template>

<script>
import upload from './upload.vue'
import { services } from '../utils'
import { uploadService } from '../utils'
import {mapGetters} from 'vuex'

export default {
    data () {
        return {
            options: [
                {
                    value: 'op1',
                    label: 'Select local file (pdf)'
                },
                {
                    value: 'op2',
                    label: 'Paste text'
                },
                {
                    value: 'op3',
                    label: 'Input a URL'
                }
            ],
            value: '',
            pastearea: '',
            URLarea: '',
            formData: Object
        }
    },
    components: {
        upload
    },
    methods: {
        getFormData (data) {
            this.formData = data;
        },
        submit () {
            this.$store.dispatch('dataModule/setLoading', true);
            if (this.value == 'op1') {
                uploadService.upload(this.formData).then(response => console.log(response));
            }
            else if (this.value == 'op2') {
                services.sendPasteText(this.pastearea).then(
                    response => {
                        //var data = {};
                        //this.$store.dispatch('dataModule/getResData', data);
                        //console.log(data);
                        console.log(this.$store.getters.resData);
                    });
                
                    //.then(
                    //    answer => {
                    //        console.log(answer)
                    //    },
                    //    error => {
                    //        console.log(error)
                    //    }
                    //);
            }
            else if (this.value == 'op3') {
                services.sendURL(this.URLarea)
                    //.then(
                    //    answer => {
                    //        console.log(answer)
                    //    },
                    //    error => {
                    //        console.log(error)
                    //    }
                    //);
            }
        }
    }
}
</script>

<style scoped>
.select {
    margin-top: 30px;
    width: 60%;
    margin-bottom: 20px;
}

.input-part {
    height: 200px;
}

.paste-part {
    width: 90%;
}

.URL-part {
    width: 90%;
}

.submit {
    /* position: absolute; */
    margin-top: 50px;
}
</style>
