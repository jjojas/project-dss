import axios from 'axios'
import { apiUrl } from "../config.json";

const apiEndpoint = apiUrl + 'recommend';

export function recommend(data, booksId) {
    return axios({
        method: 'post',
        url: apiEndpoint,
        data: {
          tags : data.tags,
          books : booksId

      }});
}
