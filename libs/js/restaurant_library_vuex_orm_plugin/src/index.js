import VuexORM from "@vuex-orm/core"
import { User, users } from "./models/User"
import { Profile, profiles }  from "./models/Profile"
import Address from "./models/Address"
import Restaurant from "./models/Restaurant"
import Table from "./models/Table"
import Seat from "./models/Seat"

import axios from 'axios';
import VuexOrmJsonApi, {RestfulActionsMixin} from '@lunity-dev/vuex-orm-json-api';
import Cookies from 'js-cookie'

const Database = new VuexORM.Database()

// Define axios defaults
axios.defaults.headers['Content-Type'] = 'application/vnd.api+json';
axios.defaults.withCredentials = true;

axios.interceptors.request.use(config => {
    config.headers['X-CSRFToken'] = Cookies.get('csrftoken');
    return config;
})

// VuexOrmJsonApi is currently used to deserialize the jsonApiFormat to models
VuexORM.use(VuexOrmJsonApi, {axios, mixins: [RestfulActionsMixin], apiRoot: process.env.VUE_APP_BASE_API_URL })


export { 
    VuexORM, 
    Database, 
    User, users, 
    Profile, profiles, 
    Address,
    Restaurant,
    Table,
    Seat
}