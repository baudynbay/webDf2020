import { Component, OnInit } from '@angular/core';
import {CompanyService} from '../company.service';
import {AuthService} from '../auth.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  username: string;
  password: string;

  constructor(
    private router: Router,
    private companyService: CompanyService,
    private authService: AuthService
  ) { }

  ngOnInit(): void {
  }

  login() {
    this.authService.login(this.username, this.password)
      .subscribe(
        response => {
          localStorage.setItem('token', response.token);
          this.router.navigate(['companies']);
        },
        error => console.log(error)
      );
  }

}
