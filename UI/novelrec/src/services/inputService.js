import axios from 'axios'
import { apiUrl } from "../config.json";

const apiEndpoint = apiUrl + 'login';

export function login(user) {
    return axios({
        method: 'post',
        url: apiEndpoint,
        data: {
          username: user.username,
          password: user.password
        }
      });
}
