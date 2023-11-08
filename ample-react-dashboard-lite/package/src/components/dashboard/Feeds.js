import React from "react";
// import record from "./test.json";
import {
  Card,
  CardBody,
  CardTitle,
  ListGroup,
  CardSubtitle,
  ListGroupItem,
  Button,
} from "reactstrap";

const FeedData = [
  {
    title: "OpenAI",
    icon: "bi bi-bell",
    color: "primary",
    date: "2 days ago",
  },
  {
    title: "Facebook",
    icon: "bi bi-person",
    color: "info",
    date: "3 days ago",
  },
  {
    title: "Company #3",
    icon: "bi bi-hdd",
    color: "danger",
    date: "5 days ago",
  },
  {
    title: "Company #4",
    icon: "bi bi-bag-check",
    color: "success",
    date: "7 days ago",
  },
  {
    title: "Company #5",
    icon: "bi bi-bell",
    color: "dark",
    date: "8 days ago",
  },

];

const Feeds = () => {
  return (
    <Card>
      <CardBody>
        <CardTitle tag="h5">Feeds</CardTitle>
        <CardSubtitle className="mb-2 text-muted" tag="h6">
          Recent updates on companies
        </CardSubtitle>
        <ListGroup flush className="mt-4">
          {FeedData.map((feed, index) => (
            <ListGroupItem
              key={index}
              action
              href="/"
              tag="a"
              className="d-flex align-items-center p-3 border-0"
            >
              <Button
                className="rounded-circle me-3"
                size="sm"
                color={feed.color}
              >
                <i className={feed.icon}></i>
              </Button>
              {feed.title}
              <small className="ms-auto text-muted text-small">
                {feed.date}
              </small>
            </ListGroupItem>
          ))}
        </ListGroup>
      </CardBody>
    </Card>
  );
};

export default Feeds;
