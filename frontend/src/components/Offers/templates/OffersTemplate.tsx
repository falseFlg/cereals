import React from "react";
import { useParams } from "react-router-dom";
import { IRouteParams } from "../../../utils/models";
import { getOffersRoutes } from "../navigation";

export const OffersTemplate: React.FC = () => {
  const { id }: IRouteParams = useParams() || {};
  return getOffersRoutes({ id });
};
