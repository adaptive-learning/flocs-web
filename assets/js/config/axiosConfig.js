var axios = require("axios");
var axiosDefaults = require("axios/lib/defaults");

axiosDefaults.xsrfCookieName = "csrftoken"
axiosDefaults.xsrfHeaderName = "X-CSRFToken"