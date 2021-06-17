import React from "react";
import { Switch } from "react-router-dom";
import { routes } from "../../routes/consts";
import { TAppNavItem } from "../../routes/models";
import { ProtectedRoute } from "../../routes/ProtectedRoute";
import { RedirectToFirstAvailable } from "../../routes/RedirectToFirstAvailable";
import { OffersListPage } from "./pages/OffersListPage";

export const getDealingsNavigation = (): TAppNavItem[] => [
  {
    allowed: [],
    path: routes.offers.list.path,
    route: {
      exact: true,
      render: () => <OffersListPage />,
    },
  },
];

export const getDealingsRoutes = () => {
  const dealingsNavigation = getDealingsNavigation();

  return (
    <Switch>
      {dealingsNavigation.map((item: TAppNavItem) => (
        <ProtectedRoute
          allowed={item.allowed}
          key={item.path}
          exact={item.route.exact}
          path={item.path}
          render={item.route.render}
        />
      ))}
      <RedirectToFirstAvailable nav={dealingsNavigation} />
    </Switch>
  );
};
