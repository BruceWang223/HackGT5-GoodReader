import config from 'config';
import * as axios from 'axios';

import { store } from '../store'

export const uploadService = {
    upload
};

// const apiUrl = 'http://localhost:3000';

function upload (formData) {
    return axios({
        method: 'POST',
        url: `${config.apiUrl}/upload`,
        data: formData,
        config: { headers: {'Content-Type': 'multipart/form-data' }}
    }).then(function(response) {
    	store.dispatch('dataModule/setResData', response.data)});
}