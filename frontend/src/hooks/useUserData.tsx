import { useQuery } from "react-query";
import { daylesfordService } from "../services";

const AUTH_DATA_QUERY_KEY = "AUTH_DATA_QUERY_KEY";

export const useUserData = (request: any) => {
  const result = useQuery<any>(
    AUTH_DATA_QUERY_KEY,
    () => daylesfordService.login(request),
    {
      enabled: false,
      refetchOnWindowFocus: false,
      retry: false,
    }
  );

  return result;
};
