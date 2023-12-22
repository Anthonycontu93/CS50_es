#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    float greysc;

    for (int i=0; i<height; i++)
    {
        for(int j=0; j<width; j++)
        {
        greysc = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed)/3.0;
        greysc = round(greysc);

            image[i][j].rgbtBlue = greysc;
            image[i][j].rgbtGreen = greysc;
            image[i][j].rgbtRed = greysc;

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
        RGBTRIPLE tmp;
        RGBTRIPLE tmp2;

for (int i=0; i<height; i++)
{
    for(int j=0; j<(width / 2); j++)
    {


        tmp = image[i][(width-1)-j];
        tmp2 = image[i][j];
        image[i][j] = tmp;
        image[i][(width-1)-j] = tmp2;

    }

}

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
  float blue;
  float green;
  float red;
  int items;

  RGBTRIPLE image_tmp[height][width];

  for (int i=0; i<height; i++)
  {
    for (int j=0; j<width; j++)
    {
        blue = 0;
        green = 0;
        red = 0;
        items = 0;

        for (int h= -1; h < 2; h++)
        {
            for (int w= -1; w < 2; w++)
            {
                if((i + h > -1) && (i + h < height) && (j + w > -1) && (j + w < width))
                {
                        blue += image[i + h][j + w].rgbtBlue;
                        green += image[i + h][j + w].rgbtGreen;
                        red += image[i + h][j + w].rgbtRed;
                        items++;
                }
            }
        }


        blue = blue / items;
        green = green / items;
        red = red / items;

        //Assign values to each pixel of the temporary image
        image_tmp[i][j].rgbtBlue = round(blue);
        image_tmp[i][j].rgbtGreen = round(green);
        image_tmp[i][j].rgbtRed = round(red);

    }
  }
       for (int i = 0; i < height; i++)
       {
         for (int j = 0; j < width; j++)
          {
            image[i][j] = image_tmp[i][j];
          }
        }


    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
     // declare an object image_copy to store intermediate values without changing the values in original image
    RGBTRIPLE image_copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // variavles to calculate Gx and Gy value for red, blue and green pixel value
            float sumred_x = 0;
            float sumblue_x = 0;
            float sumgreen_x = 0;

            float sumred_y = 0;
            float sumblue_y = 0;
            float sumgreen_y = 0;
            float sumred, sumblue, sumgreen;

            // figure out values to interae through to find the required avg
            int prv_row = i - 1;
            int next_row = i + 1;
            int prv_coloumn = j - 1;
            int next_coloumn = j + 1;
            // take care of boundary cases i.e, cases where no. of pixels surrounding current pixel is less than 8
            if (prv_row < 0)
            {
                prv_row = 0;
            }
            if (next_row >= height)
            {
                next_row = height - 1;
            }
            if (prv_coloumn < 0)
            {
                prv_coloumn = 0;
            }
            if (next_coloumn >= width)
            {
                next_coloumn = width - 1;
            }

            // interate through surrounding pixels to calculate the weighted avg
            for (int k = prv_row; k <= next_row; k++)
            {
                for (int l = prv_coloumn; l <= next_coloumn; l++)
                {
                    // calculate the factor each pixel should be multiplied with before adding to the sum
                    int x, y;
                    x = l - j;
                    y = k - i;
                    if (x == 0)
                    {
                        y *= 2;
                    }
                    if (y == 0)
                    {
                        x *= 2;
                    }
                    sumred_x += x * image[k][l].rgbtRed;
                    sumblue_x += x * image[k][l].rgbtBlue;
                    sumgreen_x += x * image[k][l].rgbtGreen;

                    sumred_y += y * image[k][l].rgbtRed;
                    sumblue_y += y * image[k][l].rgbtBlue;
                    sumgreen_y += y * image[k][l].rgbtGreen;

                }
            }
            // finally calculate the final value for each pixel by taking sqare root of Gx^2 + Gy^2
            sumred = sqrt(pow(sumred_x, 2) + pow(sumred_y, 2));
            sumblue = sqrt(pow(sumblue_x, 2) + pow(sumblue_y, 2));
            sumgreen = sqrt(pow(sumgreen_x, 2) + pow(sumgreen_y, 2));

            // cap the values to 255
            if (sumred > 255)
            {
                sumred = 255;
            }
            if (sumblue > 255)
            {
                sumblue = 255;
            }
            if (sumgreen > 255)
            {
                sumgreen = 255;
            }
            // save the weighted avg values in image_copy
            image_copy[i][j].rgbtRed = (BYTE)(round(sumred));
            image_copy[i][j].rgbtBlue = (BYTE)(round(sumblue));
            image_copy[i][j].rgbtGreen = (BYTE)(round(sumgreen));
        }
    }
    // overwrite values in image by new values
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = image_copy[i][j];
        }
    }
    return;
}
