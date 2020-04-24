import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {CompanyService} from '../company.service';
import {Company} from '../models';

@Component({
  selector: 'app-news-page',
  templateUrl: './company-page.component.html',
  styleUrls: ['./company-page.component.css']
})
export class CompanyPageComponent implements OnInit {
  company: Company;

  constructor(private categoryService: CompanyService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getCategory();
  }

  getCategory() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.categoryService.getCategory(id).subscribe(company => this.company = company);
  }

}
