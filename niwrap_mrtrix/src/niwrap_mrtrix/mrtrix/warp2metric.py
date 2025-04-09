# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

WARP2METRIC_METADATA = Metadata(
    id="eefc64bdbf00cdc4394ee65fe8d05cf1a06e7ae9.boutiques",
    name="warp2metric",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


Warp2metricFcParameters = typing.TypedDict('Warp2metricFcParameters', {
    "__STYX_TYPE__": typing.Literal["fc"],
    "template_fixel_directory": InputPathType,
    "output_fixel_directory": str,
    "output_fixel_data": str,
})


Warp2metricConfigParameters = typing.TypedDict('Warp2metricConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


Warp2metricParameters = typing.TypedDict('Warp2metricParameters', {
    "__STYX_TYPE__": typing.Literal["warp2metric"],
    "fc": typing.NotRequired[Warp2metricFcParameters | None],
    "jmat": typing.NotRequired[str | None],
    "jdet": typing.NotRequired[str | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Warp2metricConfigParameters] | None],
    "help": bool,
    "version": bool,
    "in": InputPathType,
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
        "warp2metric": warp2metric_cargs,
        "fc": warp2metric_fc_cargs,
        "config": warp2metric_config_cargs,
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
        "warp2metric": warp2metric_outputs,
    }.get(t)


def warp2metric_fc_params(
    template_fixel_directory: InputPathType,
    output_fixel_directory: str,
    output_fixel_data: str,
) -> Warp2metricFcParameters:
    """
    Build parameters.
    
    Args:
        template_fixel_directory: use an input template fixel image to define\
            fibre orientations and output a fixel image describing the change in\
            fibre cross-section (FC) in the perpendicular plane to the fixel\
            orientation. e.g. warp2metric warp.mif -fc fixel_template_directory\
            output_fixel_directory fc.mif.
        output_fixel_directory: use an input template fixel image to define\
            fibre orientations and output a fixel image describing the change in\
            fibre cross-section (FC) in the perpendicular plane to the fixel\
            orientation. e.g. warp2metric warp.mif -fc fixel_template_directory\
            output_fixel_directory fc.mif.
        output_fixel_data: use an input template fixel image to define fibre\
            orientations and output a fixel image describing the change in fibre\
            cross-section (FC) in the perpendicular plane to the fixel orientation.\
            e.g. warp2metric warp.mif -fc fixel_template_directory\
            output_fixel_directory fc.mif.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fc",
        "template_fixel_directory": template_fixel_directory,
        "output_fixel_directory": output_fixel_directory,
        "output_fixel_data": output_fixel_data,
    }
    return params


def warp2metric_fc_cargs(
    params: Warp2metricFcParameters,
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
    cargs.append("-fc")
    cargs.append(execution.input_file(params.get("template_fixel_directory")))
    cargs.append(params.get("output_fixel_directory"))
    cargs.append(params.get("output_fixel_data"))
    return cargs


def warp2metric_config_params(
    key: str,
    value: str,
) -> Warp2metricConfigParameters:
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


def warp2metric_config_cargs(
    params: Warp2metricConfigParameters,
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


class Warp2metricOutputs(typing.NamedTuple):
    """
    Output object returned when calling `warp2metric(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    jmat: OutputPathType | None
    """output a Jacobian matrix image stored in column-major order along the 4th
    dimension.Note the output jacobian describes the warp gradient w.r.t the
    scanner space coordinate system """
    jdet: OutputPathType | None
    """output the Jacobian determinant instead of the full matrix """


def warp2metric_params(
    in_: InputPathType,
    fc: Warp2metricFcParameters | None = None,
    jmat: str | None = None,
    jdet: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Warp2metricConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Warp2metricParameters:
    """
    Build parameters.
    
    Args:
        in_: the input deformation field.
        fc: use an input template fixel image to define fibre orientations and\
            output a fixel image describing the change in fibre cross-section (FC)\
            in the perpendicular plane to the fixel orientation. e.g. warp2metric\
            warp.mif -fc fixel_template_directory output_fixel_directory fc.mif.
        jmat: output a Jacobian matrix image stored in column-major order along\
            the 4th dimension.Note the output jacobian describes the warp gradient\
            w.r.t the scanner space coordinate system.
        jdet: output the Jacobian determinant instead of the full matrix.
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
        "__STYXTYPE__": "warp2metric",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "in": in_,
    }
    if fc is not None:
        params["fc"] = fc
    if jmat is not None:
        params["jmat"] = jmat
    if jdet is not None:
        params["jdet"] = jdet
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def warp2metric_cargs(
    params: Warp2metricParameters,
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
    cargs.append("warp2metric")
    if params.get("fc") is not None:
        cargs.extend(dyn_cargs(params.get("fc")["__STYXTYPE__"])(params.get("fc"), execution))
    if params.get("jmat") is not None:
        cargs.extend([
            "-jmat",
            params.get("jmat")
        ])
    if params.get("jdet") is not None:
        cargs.extend([
            "-jdet",
            params.get("jdet")
        ])
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
    cargs.append(execution.input_file(params.get("in")))
    return cargs


def warp2metric_outputs(
    params: Warp2metricParameters,
    execution: Execution,
) -> Warp2metricOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Warp2metricOutputs(
        root=execution.output_file("."),
        jmat=execution.output_file(params.get("jmat")) if (params.get("jmat") is not None) else None,
        jdet=execution.output_file(params.get("jdet")) if (params.get("jdet") is not None) else None,
    )
    return ret


def warp2metric_execute(
    params: Warp2metricParameters,
    execution: Execution,
) -> Warp2metricOutputs:
    """
    Compute fixel-wise or voxel-wise metrics from a 4D deformation field.
    
    
    
    References:
    
    Raffelt, D.; Tournier, JD/; Smith, RE.; Vaughan, DN.; Jackson, G.; Ridgway,
    GR. Connelly, A.Investigating White Matter Fibre Density and Morphology
    using Fixel-Based Analysis. Neuroimage, 2017, 144, 58-73, doi:
    10.1016/j.neuroimage.2016.09.029.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Warp2metricOutputs`).
    """
    params = execution.params(params)
    cargs = warp2metric_cargs(params, execution)
    ret = warp2metric_outputs(params, execution)
    execution.run(cargs)
    return ret


def warp2metric(
    in_: InputPathType,
    fc: Warp2metricFcParameters | None = None,
    jmat: str | None = None,
    jdet: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Warp2metricConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Warp2metricOutputs:
    """
    Compute fixel-wise or voxel-wise metrics from a 4D deformation field.
    
    
    
    References:
    
    Raffelt, D.; Tournier, JD/; Smith, RE.; Vaughan, DN.; Jackson, G.; Ridgway,
    GR. Connelly, A.Investigating White Matter Fibre Density and Morphology
    using Fixel-Based Analysis. Neuroimage, 2017, 144, 58-73, doi:
    10.1016/j.neuroimage.2016.09.029.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        in_: the input deformation field.
        fc: use an input template fixel image to define fibre orientations and\
            output a fixel image describing the change in fibre cross-section (FC)\
            in the perpendicular plane to the fixel orientation. e.g. warp2metric\
            warp.mif -fc fixel_template_directory output_fixel_directory fc.mif.
        jmat: output a Jacobian matrix image stored in column-major order along\
            the 4th dimension.Note the output jacobian describes the warp gradient\
            w.r.t the scanner space coordinate system.
        jdet: output the Jacobian determinant instead of the full matrix.
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
        NamedTuple of outputs (described in `Warp2metricOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WARP2METRIC_METADATA)
    params = warp2metric_params(
        fc=fc,
        jmat=jmat,
        jdet=jdet,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        in_=in_,
    )
    return warp2metric_execute(params, execution)


__all__ = [
    "WARP2METRIC_METADATA",
    "Warp2metricConfigParameters",
    "Warp2metricFcParameters",
    "Warp2metricOutputs",
    "Warp2metricParameters",
    "warp2metric",
    "warp2metric_config_params",
    "warp2metric_fc_params",
    "warp2metric_params",
]
