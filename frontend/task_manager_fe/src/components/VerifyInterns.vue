<template>
    <!-- navigation bar -->
    <nav class="navbar mb-3" id="navbar">
        <!-- breadcrumbs -->
        <nav aria-label="breadcrumb" id="breadcrumbs">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="#" class="text-decoration-none">My Profile</a></li>
                <li class="breadcrumb-item active" aria-current="page">Verify Intern Profiles</li>
            </ol>
        </nav>
        <div class="d-flex flex-row-reverse">
            <!-- help button -->
            <button type="button" class="btn p-2" id="help_btn">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-question-circle" viewBox="0 0 16 16">
                    <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                    <path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286m1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94"/>
                </svg>
                <i class="bi bi-question-circle"></i>
            </button>
            <!-- notification button -->
            <button type="button" class="btn p-2" id="notification_btn">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bell" viewBox="0 0 16 16">
                    <path d="M8 16a2 2 0 0 0 2-2H6a2 2 0 0 0 2 2M8 1.918l-.797.161A4 4 0 0 0 4 6c0 .628-.134 2.197-.459 3.742-.16.767-.376 1.566-.663 2.258h10.244c-.287-.692-.502-1.49-.663-2.258C12.134 8.197 12 6.628 12 6a4 4 0 0 0-3.203-3.92zM14.22 12c.223.447.481.801.78 1H1c.299-.199.557-.553.78-1C2.68 10.2 3 6.88 3 6c0-2.42 1.72-4.44 4.005-4.901a1 1 0 1 1 1.99 0A5 5 0 0 1 13 6c0 .88.32 4.2 1.22 6"/>
                </svg>
                <i class="bi bi-bell"></i>
            </button>
        </div>
    </nav>

    <div class="container">
        <!-- for elements above table -->
        <div class="d-flex">
            <div class="p-2" id="header">
                <h3>
                    New Intern Profiles
                </h3>
            </div>
            <!-- kebab menu -->
            <div class="p-2">
                <div class="dropdown">
                    <button type="button" class="btn btn-light" id="kebab_menu" data-bs-toggle="dropdown" aria-expanded="false">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-three-dots-vertical" viewBox="0 0 16 16">
                            <path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0m0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0m0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0"/>
                        </svg>
                        <i class="bi bi-three-dots-vertical"></i>
                    </button>
                    <ul class="dropdown-menu" aria-labelledby="kebab_menu">
                        <li><a class="dropdown-item" href="#">Select All</a></li>
                        <li><a class="dropdown-item" href="#">Deselect All</a></li>
                        <li><a class="dropdown-item" href="#">Verify Intern Profiles</a></li>
                        <li><a class="dropdown-item" href="#">Decline Intern Profiles</a></li>
                    </ul>
                </div>
            </div>
            <!-- search bar -->
            <div class="p-2 ms-auto">
                <div class="input-group" id="search">
                    <div class="form-outline" data-mdb-input-init>
                        <input type="search" id="form1" class="form-control" placeholder="Search">
                    </div>
                    <button type="button" class="btn btn-primary" data-mdb-ripple-init>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
                        </svg>
                        <i class="bi bi-search"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- new interns table -->
        <table class="table" id="new_interns">
            <thead>
                <th scope="col"></th>
                <th scope="col">
                    Intern Name 
                    <button type="button" class="btn btn-light" id="sort_btn">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-sort-up" viewBox="0 0 16 16">
                            <path d="M3.5 12.5a.5.5 0 0 1-1 0V3.707L1.354 4.854a.5.5 0 1 1-.708-.708l2-1.999.007-.007a.5.5 0 0 1 .7.006l2 2a.5.5 0 1 1-.707.708L3.5 3.707zm3.5-9a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5M7.5 6a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zm0 3a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1zm0 3a.5.5 0 0 0 0 1h1a.5.5 0 0 0 0-1z"/>
                        </svg>
                        <i class="bi bi-sort-up"></i>
                    </button>
                </th>
                <th scope="col">Date Submitted</th>
                <th scope="col">NDA File</th>
                <th scope="col">Action</th>
            </thead>
            <tbody>
                <tr>
                    <td><input type="checkbox"></td>
                    <td>Earl Patrick Melchor</td>
                    <td>August 5, 2023</td>
                    <td><a href="#" class="link-dark link-offset-2 link-underline-opacity-25 link-underline-opacity-75-hover">Melchor_NDA.pdf</a></td>
                    <td>
                        <div class="row">
                            <div class="col">
                                <button type="button" class="btn btn-success mx-1" id="verify_btn">Verify</button>
                                <button type="button" class="btn btn-danger" id="decline_btn">Decline</button>
                            </div>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td><input type="checkbox"></td>
                    <td>Aliya Galang</td>
                    <td>August 6, 2023</td>
                    <td><a href="#" class="link-dark link-offset-2 link-underline-opacity-25 link-underline-opacity-75-hover">Galang_NDA.pdf</a></td>
                    <td>
                        <div class="row">
                            <div class="col">
                                <button type="button" class="btn btn-success mx-1" id="verify_btn">Verify</button>
                                <button type="button" class="btn btn-danger" id="decline_btn">Decline</button>
                            </div>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td><input type="checkbox"></td>
                    <td>Hannah Erin Co</td>
                    <td>August 7, 2023</td>
                    <td><a href="#" class="link-dark link-offset-2 link-underline-opacity-25 link-underline-opacity-75-hover">Co_NDA.pdf</a></td>
                    <td>
                        <div class="row">
                            <div class="col">
                                <button type="button" class="btn btn-success mx-1" id="verify_btn">Verify</button>
                                <button type="button" class="btn btn-danger" id="decline_btn">Decline</button>
                            </div>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- pagination -->
        <div class="d-flex justify-content-end">
            <nav>
                <ul class="pagination">
                    <li class="page-item">
                        <a class="page-link" href="#" aria-label="Previous">
                            <span aria-hidden="true">&laquo;</span>
                        </a>
                    </li>
                    <li class="page-item"><a class="page-link" href="#">1</a></li>
                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                    <li class="page-item"><a class="page-link" href="#">3</a></li>
                    <li class="page-item">
                        <a class="page-link" href="#" aria-label="Next">
                            <span aria-hidden="true">&raquo;</span>
                        </a>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</template>

<script>

</script>

<style>
#navbar {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-weight: bold;
  position: fixed;
  top: 0;
  width: 59%;
  height: 50px;
  background-color: #D78888;
}
#navbar > nav {
  padding-top: 5px;
  padding-left: 25px;
}
#navbar > div {
  padding-bottom: 11px;
  padding-right: 15px;
}
.breadcrumb > li + li::before {
  --bs-breadcrumb-divider: '>';
  color: #F8FAFC !important;
}
#breadcrumbs > ol > li {
  color: #F8FAFC; 
}
#breadcrumbs > ol > li > a {
  color: #F8FAFC; 
}
#breadcrumbs > ol > li > a:hover {
  color: #b6c8da; 
}
#notification_btn {
  color: #F8FAFC;
  margin: 0 auto;
  padding: 0;
  text-align: center;
  height: 30px;
  line-height: 0px;
}
#notification_btn:hover {
  background-color: #ba5f5f;
}
#help_btn {
  color: #F8FAFC;
  margin: 0 auto;
  padding: 0;
  text-align: center;
  height: 30px;
  line-height: 0px;
}
#help_btn:hover {
  background-color: #ba5f5f;
}
#header > h3 {
    font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-weight: bold;
  color: #F27036;
}
#kebab_menu {
    font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-weight: bold;
  background-color: #FFFFFF;
  border-color: #FFFFFF;
  color: rgba(242, 112, 54, .7);
  margin: 0 auto;
  padding: 0;
}
#kebab_menu:hover {
  background-color: #cccccc;
}
#search > button {
    font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #484848;
  font-size: 11px;
  background-color: rgba(196,69, 69, .4);
  border-color: #C44545;
  height: 30px;
}
#search > div > input {
    font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  border-color: #C44545;
  border-radius: 6px 0px 0px 6px;
  width: 200px;
  height: 30px;
}
#search > div > input:focus {
  outline: none !important;
  border-color: #C44545;
  box-shadow: 0 0 10px #C44545;
}
#new_interns th {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #EA580C;
  color: #F8FAFC;
}
#sort_btn {
  text-align: center;
  background-color: #EA580C;
  border-color: #EA580C;
  color: #F8FAFC;
  width: 30px;
  margin: 0 auto;
  padding: 0;
}
#sort_btn:hover {
  background-color: #a94c1b;
}
#new_interns td {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
#new_interns td:nth-child(2) {
  text-align: left;
}
#verify_btn {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 14px;
  width: 80px;
  height: 30px;
  margin: 0 auto;
  padding: 0;
  background-color: #22C55E;
  border-color: #22C55E;
}
#verify_btn:hover {
  background-color: #28914f;
}
#decline_btn {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 14px;
  width: 80px;
  height: 30px;
  margin: 0 auto;
  padding: 0;
  background-color: #EF4444;
  border-color: #EF4444;
}
#decline_btn:hover {
  background-color: #ce2828;
}
.page-item > a {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; 
  color: #000000;
}
.pagination a:active {
  background-color: #D78888;
  color: #F8FAFC;
}
.pagination a:focus {
  background-color: #FFFFFF;
  color: #000000;
  box-shadow: 0 0 0px;
}
.pagination a:hover:not(:active) {
  background-color: #ddd;
  color: #000000;
}
</style>