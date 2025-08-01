# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DWI2MASK_METADATA = Metadata(
    id="9d585c1eb8931fbf6a7b9b4efcfcbe79a0ec151f.boutiques",
    name="dwi2mask",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


Dwi2maskFslgradParameters = typing.TypedDict('Dwi2maskFslgradParameters', {
    "__STYXTYPE__": typing.Literal["fslgrad"],
    "bvecs": InputPathType,
    "bvals": InputPathType,
})


Dwi2maskConfigParameters = typing.TypedDict('Dwi2maskConfigParameters', {
    "__STYXTYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


Dwi2maskParameters = typing.TypedDict('Dwi2maskParameters', {
    "__STYXTYPE__": typing.Literal["dwi2mask"],
    "clean_scale": typing.NotRequired[int | None],
    "grad": typing.NotRequired[InputPathType | None],
    "fslgrad": typing.NotRequired[Dwi2maskFslgradParameters | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Dwi2maskConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": InputPathType,
    "output": str,
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
        "dwi2mask": dwi2mask_cargs,
        "fslgrad": dwi2mask_fslgrad_cargs,
        "config": dwi2mask_config_cargs,
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
        "dwi2mask": dwi2mask_outputs,
    }.get(t)


def dwi2mask_fslgrad_params(
    bvecs: InputPathType,
    bvals: InputPathType,
) -> Dwi2maskFslgradParameters:
    """
    Build parameters.
    
    Args:
        bvecs: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
        bvals: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslgrad",
        "bvecs": bvecs,
        "bvals": bvals,
    }
    return params


def dwi2mask_fslgrad_cargs(
    params: Dwi2maskFslgradParameters,
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
    cargs.append("-fslgrad")
    cargs.append(execution.input_file(params.get("bvecs")))
    cargs.append(execution.input_file(params.get("bvals")))
    return cargs


def dwi2mask_config_params(
    key: str,
    value: str,
) -> Dwi2maskConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def dwi2mask_config_cargs(
    params: Dwi2maskConfigParameters,
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
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


class Dwi2maskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dwi2mask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output whole-brain mask image"""


def dwi2mask_params(
    input_: InputPathType,
    output: str,
    clean_scale: int | None = None,
    grad: InputPathType | None = None,
    fslgrad: Dwi2maskFslgradParameters | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Dwi2maskConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Dwi2maskParameters:
    """
    Build parameters.
    
    Args:
        input_: the input DWI image containing volumes that are both diffusion\
            weighted and b=0.
        output: the output whole-brain mask image.
        clean_scale: the maximum scale used to cut bridges. A certain maximum\
            scale cuts bridges up to a width (in voxels) of 2x the provided scale.\
            Setting this to 0 disables the mask cleaning step. (Default: 2).
        grad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in a text file. This should be supplied as a 4xN text file\
            with each line is in the format [ X Y Z b ], where [ X Y Z ] describe\
            the direction of the applied gradient, and b gives the b-value in units\
            of s/mm^2. If a diffusion gradient scheme is present in the input image\
            header, the data provided with this option will be instead used.
        fslgrad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dwi2mask",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
        "output": output,
    }
    if clean_scale is not None:
        params["clean_scale"] = clean_scale
    if grad is not None:
        params["grad"] = grad
    if fslgrad is not None:
        params["fslgrad"] = fslgrad
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def dwi2mask_cargs(
    params: Dwi2maskParameters,
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
    cargs.append("dwi2mask")
    if params.get("clean_scale") is not None:
        cargs.extend([
            "-clean_scale",
            str(params.get("clean_scale"))
        ])
    if params.get("grad") is not None:
        cargs.extend([
            "-grad",
            execution.input_file(params.get("grad"))
        ])
    if params.get("fslgrad") is not None:
        cargs.extend(dyn_cargs(params.get("fslgrad")["__STYXTYPE__"])(params.get("fslgrad"), execution))
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.append(execution.input_file(params.get("input")))
    cargs.append(params.get("output"))
    return cargs


def dwi2mask_outputs(
    params: Dwi2maskParameters,
    execution: Execution,
) -> Dwi2maskOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Dwi2maskOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def dwi2mask_execute(
    params: Dwi2maskParameters,
    execution: Execution,
) -> Dwi2maskOutputs:
    """
    Generates a whole brain mask from a DWI image.
    
    All diffusion weighted and b=0 volumes are used to obtain a mask that
    includes both brain tissue and CSF.
    
    In a second step peninsula-like extensions, where the peninsula itself is
    wider than the bridge connecting it to the mask, are removed. This may help
    removing artefacts and non-brain parts, e.g. eyes, from the mask.
    
    References:
    
    Dhollander T, Raffelt D, Connelly A. Unsupervised 3-tissue response function
    estimation from single-shell or multi-shell diffusion MR data without a
    co-registered T1 image. ISMRM Workshop on Breaking the Barriers of Diffusion
    MRI, 2016, 5.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Dwi2maskOutputs`).
    """
    params = execution.params(params)
    cargs = dwi2mask_cargs(params, execution)
    ret = dwi2mask_outputs(params, execution)
    execution.run(cargs)
    return ret


def dwi2mask(
    input_: InputPathType,
    output: str,
    clean_scale: int | None = None,
    grad: InputPathType | None = None,
    fslgrad: Dwi2maskFslgradParameters | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Dwi2maskConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Dwi2maskOutputs:
    """
    Generates a whole brain mask from a DWI image.
    
    All diffusion weighted and b=0 volumes are used to obtain a mask that
    includes both brain tissue and CSF.
    
    In a second step peninsula-like extensions, where the peninsula itself is
    wider than the bridge connecting it to the mask, are removed. This may help
    removing artefacts and non-brain parts, e.g. eyes, from the mask.
    
    References:
    
    Dhollander T, Raffelt D, Connelly A. Unsupervised 3-tissue response function
    estimation from single-shell or multi-shell diffusion MR data without a
    co-registered T1 image. ISMRM Workshop on Breaking the Barriers of Diffusion
    MRI, 2016, 5.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input DWI image containing volumes that are both diffusion\
            weighted and b=0.
        output: the output whole-brain mask image.
        clean_scale: the maximum scale used to cut bridges. A certain maximum\
            scale cuts bridges up to a width (in voxels) of 2x the provided scale.\
            Setting this to 0 disables the mask cleaning step. (Default: 2).
        grad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in a text file. This should be supplied as a 4xN text file\
            with each line is in the format [ X Y Z b ], where [ X Y Z ] describe\
            the direction of the applied gradient, and b gives the b-value in units\
            of s/mm^2. If a diffusion gradient scheme is present in the input image\
            header, the data provided with this option will be instead used.
        fslgrad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Dwi2maskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DWI2MASK_METADATA)
    params = dwi2mask_params(
        clean_scale=clean_scale,
        grad=grad,
        fslgrad=fslgrad,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        input_=input_,
        output=output,
    )
    return dwi2mask_execute(params, execution)


__all__ = [
    "DWI2MASK_METADATA",
    "Dwi2maskConfigParameters",
    "Dwi2maskFslgradParameters",
    "Dwi2maskOutputs",
    "Dwi2maskParameters",
    "dwi2mask",
    "dwi2mask_config_params",
    "dwi2mask_fslgrad_params",
    "dwi2mask_params",
]
