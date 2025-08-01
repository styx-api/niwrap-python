# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FIRST_FLIRT_METADATA = Metadata(
    id="78b8e402b6c5d5ad75e5df439dee86b237fbb0a6.boutiques",
    name="first_flirt",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FirstFlirtParameters = typing.TypedDict('FirstFlirtParameters', {
    "__STYXTYPE__": typing.Literal["first_flirt"],
    "input_image": InputPathType,
    "output_basename": str,
    "already_brain_extracted_flag": bool,
    "debug_flag": bool,
    "inweight_flag": bool,
    "strucweight_mask": typing.NotRequired[InputPathType | None],
    "cort_flag": bool,
    "cost_function": typing.NotRequired[str | None],
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
        "first_flirt": first_flirt_cargs,
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
        "first_flirt": first_flirt_outputs,
    }.get(t)


class FirstFlirtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `first_flirt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    registered_output_image: OutputPathType
    """Output image registered to standard space"""
    log_file: OutputPathType
    """Log file containing details of the registration process"""
    transformation_matrix: OutputPathType
    """Transformation matrix file"""


def first_flirt_params(
    input_image: InputPathType,
    output_basename: str,
    already_brain_extracted_flag: bool = False,
    debug_flag: bool = False,
    inweight_flag: bool = False,
    strucweight_mask: InputPathType | None = None,
    cort_flag: bool = False,
    cost_function: str | None = None,
) -> FirstFlirtParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input image (e.g. subject10rawT1.nii.gz).
        output_basename: Output basename for the results (e.g.\
            subject10rawT1_to_std_sub).
        already_brain_extracted_flag: Input is already brain extracted.
        debug_flag: Debug mode: don't delete intermediate files.
        inweight_flag: Use a weighting mask on the first registration.
        strucweight_mask: Use a specific structure weighting mask (in standard\
            space) for an optional third-stage registration step (e.g.\
            maskimage.nii.gz).
        cort_flag: Use a weighting mask of the whole brain on the first\
            registration for specific models.
        cost_function: Specify the cost function to be used by all FLIRT calls.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "first_flirt",
        "input_image": input_image,
        "output_basename": output_basename,
        "already_brain_extracted_flag": already_brain_extracted_flag,
        "debug_flag": debug_flag,
        "inweight_flag": inweight_flag,
        "cort_flag": cort_flag,
    }
    if strucweight_mask is not None:
        params["strucweight_mask"] = strucweight_mask
    if cost_function is not None:
        params["cost_function"] = cost_function
    return params


def first_flirt_cargs(
    params: FirstFlirtParameters,
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
    cargs.append("first_flirt")
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_basename"))
    if params.get("already_brain_extracted_flag"):
        cargs.append("-b")
    if params.get("debug_flag"):
        cargs.append("-d")
    if params.get("inweight_flag"):
        cargs.append("-inweight")
    if params.get("strucweight_mask") is not None:
        cargs.extend([
            "-strucweight",
            execution.input_file(params.get("strucweight_mask"))
        ])
    if params.get("cort_flag"):
        cargs.append("-cort")
    if params.get("cost_function") is not None:
        cargs.extend([
            "-cost",
            params.get("cost_function")
        ])
    return cargs


def first_flirt_outputs(
    params: FirstFlirtParameters,
    execution: Execution,
) -> FirstFlirtOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FirstFlirtOutputs(
        root=execution.output_file("."),
        registered_output_image=execution.output_file(params.get("output_basename") + "_result.nii.gz"),
        log_file=execution.output_file(params.get("output_basename") + "_log.txt"),
        transformation_matrix=execution.output_file(params.get("output_basename") + "_matrix.mat"),
    )
    return ret


def first_flirt_execute(
    params: FirstFlirtParameters,
    execution: Execution,
) -> FirstFlirtOutputs:
    """
    FLIRT-based image registration tool with additional options for brain extraction
    and weighting masks.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FirstFlirtOutputs`).
    """
    params = execution.params(params)
    cargs = first_flirt_cargs(params, execution)
    ret = first_flirt_outputs(params, execution)
    execution.run(cargs)
    return ret


def first_flirt(
    input_image: InputPathType,
    output_basename: str,
    already_brain_extracted_flag: bool = False,
    debug_flag: bool = False,
    inweight_flag: bool = False,
    strucweight_mask: InputPathType | None = None,
    cort_flag: bool = False,
    cost_function: str | None = None,
    runner: Runner | None = None,
) -> FirstFlirtOutputs:
    """
    FLIRT-based image registration tool with additional options for brain extraction
    and weighting masks.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_image: Input image (e.g. subject10rawT1.nii.gz).
        output_basename: Output basename for the results (e.g.\
            subject10rawT1_to_std_sub).
        already_brain_extracted_flag: Input is already brain extracted.
        debug_flag: Debug mode: don't delete intermediate files.
        inweight_flag: Use a weighting mask on the first registration.
        strucweight_mask: Use a specific structure weighting mask (in standard\
            space) for an optional third-stage registration step (e.g.\
            maskimage.nii.gz).
        cort_flag: Use a weighting mask of the whole brain on the first\
            registration for specific models.
        cost_function: Specify the cost function to be used by all FLIRT calls.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FirstFlirtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIRST_FLIRT_METADATA)
    params = first_flirt_params(
        input_image=input_image,
        output_basename=output_basename,
        already_brain_extracted_flag=already_brain_extracted_flag,
        debug_flag=debug_flag,
        inweight_flag=inweight_flag,
        strucweight_mask=strucweight_mask,
        cort_flag=cort_flag,
        cost_function=cost_function,
    )
    return first_flirt_execute(params, execution)


__all__ = [
    "FIRST_FLIRT_METADATA",
    "FirstFlirtOutputs",
    "FirstFlirtParameters",
    "first_flirt",
    "first_flirt_params",
]
