# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MULTIPLY_IMAGES_METADATA = Metadata(
    id="b6e8db4f48e2712b28e3d2e665c15294bd29849c.boutiques",
    name="MultiplyImages",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


MultiplyImagesParameters = typing.TypedDict('MultiplyImagesParameters', {
    "__STYXTYPE__": typing.Literal["MultiplyImages"],
    "dimension": typing.Literal[3, 2],
    "first_input": InputPathType,
    "second_input": typing.NotRequired[InputPathType | None],
    "second_input_2": typing.NotRequired[float | None],
    "output_product_image": str,
    "num_threads": typing.NotRequired[int | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "MultiplyImages": multiply_images_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "MultiplyImages": multiply_images_outputs,
    }.get(t)


class MultiplyImagesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `multiply_images(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_product_image_outfile: OutputPathType
    """Average image file."""


def multiply_images_params(
    dimension: typing.Literal[3, 2],
    first_input: InputPathType,
    output_product_image: str,
    second_input: InputPathType | None = None,
    second_input_2: float | None = None,
    num_threads: int | None = 1,
) -> MultiplyImagesParameters:
    """
    Build parameters.
    
    Args:
        dimension: 3 or 2. Image dimension (2 or 3).
        first_input: Image 1.
        output_product_image: Outputfname.nii.gz: the name of the resulting\
            image.
        second_input: file or string or a float. Image 2 or multiplication\
            weight.
        second_input_2: file or string or a float. Image 2 or multiplication\
            weight.
        num_threads: Number of itk threads to use.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "MultiplyImages",
        "dimension": dimension,
        "first_input": first_input,
        "output_product_image": output_product_image,
    }
    if second_input is not None:
        params["second_input"] = second_input
    if second_input_2 is not None:
        params["second_input_2"] = second_input_2
    if num_threads is not None:
        params["num_threads"] = num_threads
    return params


def multiply_images_cargs(
    params: MultiplyImagesParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("MultiplyImages")
    cargs.append(str(params.get("dimension")))
    cargs.append(execution.input_file(params.get("first_input")))
    if params.get("second_input") is not None:
        cargs.append(execution.input_file(params.get("second_input")))
    if params.get("second_input_2") is not None:
        cargs.append(str(params.get("second_input_2")))
    cargs.append(params.get("output_product_image"))
    if params.get("num_threads") is not None:
        cargs.append(str(params.get("num_threads")))
    return cargs


def multiply_images_outputs(
    params: MultiplyImagesParameters,
    execution: Execution,
) -> MultiplyImagesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MultiplyImagesOutputs(
        root=execution.output_file("."),
        output_product_image_outfile=execution.output_file(params.get("output_product_image")),
    )
    return ret


def multiply_images_execute(
    params: MultiplyImagesParameters,
    execution: Execution,
) -> MultiplyImagesOutputs:
    """
    Multiply 2 images; 2nd image file may also be floating point numerical value,
    and program will act accordingly -- i.e. read as a number. Program handles
    vector and tensor images as well.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MultiplyImagesOutputs`).
    """
    params = execution.params(params)
    cargs = multiply_images_cargs(params, execution)
    ret = multiply_images_outputs(params, execution)
    execution.run(cargs)
    return ret


def multiply_images(
    dimension: typing.Literal[3, 2],
    first_input: InputPathType,
    output_product_image: str,
    second_input: InputPathType | None = None,
    second_input_2: float | None = None,
    num_threads: int | None = 1,
    runner: Runner | None = None,
) -> MultiplyImagesOutputs:
    """
    Multiply 2 images; 2nd image file may also be floating point numerical value,
    and program will act accordingly -- i.e. read as a number. Program handles
    vector and tensor images as well.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        dimension: 3 or 2. Image dimension (2 or 3).
        first_input: Image 1.
        output_product_image: Outputfname.nii.gz: the name of the resulting\
            image.
        second_input: file or string or a float. Image 2 or multiplication\
            weight.
        second_input_2: file or string or a float. Image 2 or multiplication\
            weight.
        num_threads: Number of itk threads to use.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MultiplyImagesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MULTIPLY_IMAGES_METADATA)
    params = multiply_images_params(
        dimension=dimension,
        first_input=first_input,
        second_input=second_input,
        second_input_2=second_input_2,
        output_product_image=output_product_image,
        num_threads=num_threads,
    )
    return multiply_images_execute(params, execution)


__all__ = [
    "MULTIPLY_IMAGES_METADATA",
    "MultiplyImagesOutputs",
    "MultiplyImagesParameters",
    "multiply_images",
    "multiply_images_params",
]
