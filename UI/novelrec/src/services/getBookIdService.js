import axios from 'axios'
import { apiUrl } from "../config.json";

const apiEndpoint = apiUrl + 'book/';

export function getBookId(data) {
    return axios({
        method: 'get',
        url: apiEndpoint,
        data: {
          books : data.books
      }});
}
