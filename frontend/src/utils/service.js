import config from 'config';

import global_ from '../components/global'

import { store } from '../store'

export const services = {
    sendURL,
    sendPasteText,
    sendFileContent
};

// const apiUrl = 'http://localhost:3000';

function sendURL (content) {
    const requestOptions = {
        method: 'POST',
        credentials: 'include',
        headers: { 'Content-Type': 'application/json',
        },
        body: JSON.stringify({'type': 0,
        'content': content})
    };

    // return fetch(`${config.apiUrl}/data`, requestOptions).then(handleResponse);
    return fetch(`${config.apiUrl}/data`, requestOptions).then(function(response) {
        // The response is a Response instance.
        // You parse the data into a useable format using `.json()`
        return response.json();
    }).then(function(data) {
        console.log(data);
        store.dispatch('dataModule/setResData', data);
        // console.log(store.getters.resData);
        // `data` is the parsed version of the JSON returned from the above endpoint.
        // console.log(data);  // { "userId": 1, "id": 1, "title": "...", "body": "..." }
    });
}

function sendPasteText (content) {
    const requestOptions = {
        method: 'POST',
        // credentials: 'include',
        headers: { 'Content-Type': 'application/json',
        },
        body: JSON.stringify({'type': 1,
        'content': content})
    };


    return fetch(`${config.apiUrl}/data`, requestOptions).then(function(response) {
        // The response is a Response instance.
        // You parse the data into a useable format using `.json()`
        return response.json();
    }).then(function(data) {
        console.log(data);
        store.dispatch('dataModule/setResData', data);
        // `data` is the parsed version of the JSON returned from the above endpoint.
        // console.log(data);  // { "userId": 1, "id": 1, "title": "...", "body": "..." }
    });
}

function sendFileContent (content) {
    const requestOptions = {
        method: 'POST',
        credentials: 'include',
        headers: { 'Content-Type': 'application/json',
        },
        body: JSON.stringify({'type': 2,
        'content': content})
    };

    return fetch(`${config.apiUrl}/data`, requestOptions).then(response => console.log(response));
}

function handleResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(text);
        if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }
        console.log(data);
        return data;
    });
}